# Build apply-plan for the 2026-08-17 wiki-refresh.
# Adapted from build-apply-plan-2026-08-09.py. This week: twelve fresh
# sources from the R8 monitor haul (three arXiv papers, one Fed FEDS note,
# eight Ledger Insights items), all carrying on-vocabulary topics written
# by the monitors; and the 60 concept stubs in 30_Concepts/, built on
# 9 August, which the scanner sees for the first time.
# Two builder changes:
# 1. A fresh note whose existing topics are all on-vocabulary is confirmed
#    as-is (topics = existing). Six of this week's twelve would otherwise
#    have drifted under the mapper's tie-breaks (topic/law/securities or
#    topic/law in place of topic/tokenisation, topic/finance/market-
#    infrastructure alongside stablecoins). Pinning per note no longer scales.
# 2. 30_Concepts notes enter scope with wiki_role "concept". Their domain
#    field holds MOC section labels ("examples", "sub-topic") as well as
#    enum values, so topics derive from the MOCs the stub links to
#    (MOC_TOPIC) plus any enum domain value, parent-pruned, capped at 3.
import json
import re
from collections import Counter

import yaml

VAULT = "C:/Users/Simon/Documents/wiki-tokenise"
SCAN = VAULT + "/99_Meta/wiki-tokenise/wiki-scan-2026-08-17.json"
PLAN_OUT = VAULT + "/99_Meta/wiki-tokenise/apply-plan-2026-08-17.json"
INDEXED = "2026-08-17T00:00:00Z"

DOMAIN_TOPIC = {
    'finance': 'topic/finance',
    'stablecoins': 'topic/finance/stablecoins',
    'market-structure': 'topic/finance/market-infrastructure',
    'market-infrastructure': 'topic/finance/market-infrastructure',
    'blockchain-settlement': 'topic/blockchain-settlement',
    'settlement': 'topic/blockchain-settlement',
    'defi': 'topic/blockchain-settlement',
    'law': 'topic/law',
    'private-law': 'topic/law',
    'international-private-law': 'topic/law',
    'securities-law': 'topic/law/securities',
    'property-rights': 'topic/law/property-rights',
    'tokenised-deposits': 'topic/finance/tokenised-deposits',
    'cross-border-payments': 'topic/finance',
    'payment-systems': 'topic/finance',
    'monetary-policy': 'topic/finance',
    'financial-regulation': 'topic/law',
    'cbdc': 'topic/finance/cbdc',
    'agentic-ai': 'topic/agentic-ai',
    'ai-governance': 'topic/agentic-ai',
    'llm-trading': 'topic/agentic-ai',
    'carbon-credits': 'topic/carbon-credits',
    'environmental-markets': 'topic/carbon-credits',
    'real-estate': 'topic/real-estate',
}
INSTRUMENT_TOPIC = {
    'stablecoin-fiat': 'topic/finance/stablecoins',
    'stablecoin-rwa-backed': 'topic/finance/stablecoins',
    'stablecoin-algorithmic': 'topic/finance/stablecoins',
    'payment-stablecoin': 'topic/finance/stablecoins',
    'e-money-token': 'topic/finance/stablecoins',
    'asset-referenced-token': 'topic/finance/stablecoins',
    'cbdc-wholesale': 'topic/finance/cbdc',
    'cbdc-retail': 'topic/finance/cbdc',
    'security-token': 'topic/law/securities',
    'tokenised-equity': 'topic/law/securities',
    'tokenised-deposit': 'topic/finance/tokenised-deposits',
    'tokenised-bond': 'topic/finance/market-infrastructure',
    'tokenised-fund': 'topic/finance/market-infrastructure',
    'tokenised-money-market-fund': 'topic/finance/market-infrastructure',
    'tokenised-treasury': 'topic/finance/market-infrastructure',
    'tokenised-private-credit': 'topic/finance/market-infrastructure',
    'tokenised-commodity': 'topic/finance/market-infrastructure',
    'tokenised-carbon-credit': 'topic/carbon-credits',
    'tokenised-real-estate': 'topic/real-estate',
}
DOCTRINE_TOPIC = {
    'property-category': 'topic/law/property-rights',
    'transfer': 'topic/law/property-rights',
    'secured-transactions': 'topic/law/property-rights',
    'take-free-purchaser': 'topic/law/property-rights',
    'control': 'topic/law/property-rights',
    'custody': 'topic/law/property-rights',
    'market-abuse': 'topic/law/securities',
    'prospectus': 'topic/law/securities',
    'mifid-equivalence': 'topic/law/securities',
    'market-structure': 'topic/finance/market-infrastructure',
    'singleness-of-money': 'topic/finance',
    'licensing': 'topic/law',
    'aml-cft': 'topic/law',
    'disclosure': 'topic/law',
    'consumer-protection': 'topic/law',
    'intermediation': 'topic/law',
    'choice-of-law': 'topic/law',
    'insolvency': 'topic/law',
    'reserve-requirements': 'topic/law',
    'stablecoin-regulation': 'topic/finance/stablecoins',
    'federal-preemption': 'topic/law',
}
PARENT = {
    'topic/finance/stablecoins': 'topic/finance',
    'topic/finance/cbdc': 'topic/finance',
    'topic/finance/tokenised-deposits': 'topic/finance',
    'topic/finance/market-infrastructure': 'topic/finance',
    'topic/law/securities': 'topic/law',
    'topic/law/property-rights': 'topic/law',
    'topic/law/digital-assets': 'topic/law',
}
MOC_TOPIC = {
    'MOC - Carbon-Credits': 'topic/carbon-credits',
    'MOC - Agent-Ledger-Interface': 'topic/agentic-ai',
    'MOC - Agentic-AI': 'topic/agentic-ai',
    'MOC - Property-Rights': 'topic/law/property-rights',
    'MOC - Private-Law-Convergence': 'topic/law/digital-assets',
    'MOC - Finance': 'topic/finance',
    'MOC - Law': 'topic/law',
    'MOC - Blockchain-Settlement': 'topic/blockchain-settlement',
    'MOC - Stablecoins': 'topic/finance/stablecoins',
    'MOC - Real-Estate': 'topic/real-estate',
}
VOCAB = {
    'topic/tokenisation', 'topic/finance', 'topic/finance/stablecoins',
    'topic/finance/cbdc', 'topic/finance/tokenised-deposits',
    'topic/finance/market-infrastructure', 'topic/law', 'topic/law/securities',
    'topic/law/property-rights', 'topic/law/digital-assets',
    'topic/blockchain-settlement', 'topic/agentic-ai', 'topic/carbon-credits',
    'topic/real-estate',
}
# Institutional issuers -> publisher subject. Press/aggregators excluded.
ORG_SUBJECT = {
    'BIS': 'subject/bis',
    'Bank for International Settlements': 'subject/bis',
    'ESMA': 'subject/esma',
    'European Securities and Markets Authority': 'subject/esma',
    'European Securities and Markets Authority (ESMA)': 'subject/esma',
    'IMF': 'subject/imf',
    'International Monetary Fund': 'subject/imf',
    'FSB': 'subject/fsb',
    'Financial Stability Board': 'subject/fsb',
    'IOSCO': 'subject/iosco',
    'HKMA': 'subject/hkma',
    'Hong Kong Monetary Authority': 'subject/hkma',
    'HKMC': 'subject/hkmc',
    'MAS': 'subject/mas',
    'Monetary Authority of Singapore': 'subject/mas',
    'Federal Reserve': 'subject/federal-reserve',
    'Federal Reserve Board': 'subject/federal-reserve',
    'Board of Governors of the Federal Reserve System': 'subject/federal-reserve',
    'UNIDROIT': 'subject/unidroit',
    'Verra': 'subject/verra',
    'United States Congress': 'subject/congress',
}
# 30_Areas notes carry no domain/instrument/doctrine frontmatter.
# Classified by hand from their titles and bodies. Keys are filename substrings.
OVERRIDES = {
    'Storm Research': ['topic/blockchain-settlement', 'topic/finance/stablecoins'],
    'Carbon Credits as Tokenisation Test Bed': ['topic/carbon-credits', 'topic/tokenisation'],
    'Interoperability and Cross-Chain Fragmentation': ['topic/blockchain-settlement', 'topic/finance/market-infrastructure'],
    'Private Law Convergence Across Jurisdictions': ['topic/law/property-rights', 'topic/law/digital-assets'],
    'Regulatory Pathways by Jurisdiction': ['topic/law', 'topic/tokenisation'],
    'Settlement Efficiency and Cost Reduction': ['topic/blockchain-settlement', 'topic/finance/market-infrastructure'],
    'Stablecoin Architecture Evolution': ['topic/finance/stablecoins', 'topic/tokenisation'],
    'Tokenised Securities vs Real-World Assets': ['topic/law/securities', 'topic/tokenisation'],
    'Agentic AI and Tokenised Settlement Infrastructure': ['topic/agentic-ai', 'topic/blockchain-settlement', 'topic/finance/stablecoins'],
}
# Per-note pins supplying canonical topics where the mapper would drift
# from the monitor-written pair. Keys are filename substrings.
NOTE_OVERRIDES = {
    'hkma-quantum-preparedness-whitepaper-2026': ['topic/blockchain-settlement'],
    'Ledger-Insights-Circle-NY-Trust-Charter': ['topic/law'],
    'IMF-Speech-2026-08-Katz-Stablecoins-Emerging-Markets': ['topic/finance/stablecoins', 'topic/finance'],
    # Concept stubs where the MOC-derived topic misses the concept's own home.
    '30_Concepts/Tokenisation.md': ['topic/tokenisation', 'topic/finance'],
    '30_Concepts/Tokenised-Deposit.md': ['topic/finance/tokenised-deposits'],
    '30_Concepts/E-Money-Token.md': ['topic/law', 'topic/finance/stablecoins'],
    '30_Concepts/Asset-Referenced-Token.md': ['topic/law', 'topic/finance/stablecoins'],
}
QUARANTINE = []

d = json.load(open(SCAN, encoding='utf-8'))
notes = d['notes']
targets = [n for n in notes
           if n['state'] in ('fresh', 'modified')
           and n['path'].replace('\\', '/').startswith(('10_Sources', '30_Areas', '30_Concepts'))
           and not n['path'].endswith('SOURCE-REGISTER.md')
           and not any(n['path'].endswith(q) for q in QUARANTINE)]

changes = []
preview = []
for n in targets:
    fp = n['path'].replace('\\', '/')
    txt = open(VAULT + '/' + fp, encoding='utf-8').read()
    y = {}
    if txt.startswith('---'):
        try:
            y = yaml.safe_load(txt.split('---', 2)[1]) or {}
        except Exception:
            y = {}

    topics = None
    for key, override in {**OVERRIDES, **NOTE_OVERRIDES}.items():
        if key in fp:
            topics = list(override)
            break

    existing = y.get('topic') or []
    is_concept = fp.startswith('30_Concepts')

    # Fresh note carrying monitor-written, on-vocabulary topics: confirm as-is.
    if topics is None and n['state'] == 'fresh' and existing and all(t in VOCAB for t in existing):
        topics = list(existing)

    # Concept stub: topics from linked MOCs plus enum domain values.
    if topics is None and is_concept:
        score = Counter()
        for m in set(re.findall(r'\[\[(MOC - [^\]|#]+)', txt)):
            if m in MOC_TOPIC:
                score[MOC_TOPIC[m]] += 2
        for v in (y.get('domain') or []):
            if v in DOMAIN_TOPIC:
                score[DOMAIN_TOPIC[v]] += 1
        for child, par in PARENT.items():
            if child in score and par in score:
                del score[par]
        topics = [t for t, _ in score.most_common()][:3]

    # Modified note that already carries topics and has no pin: re-stamp only.
    if topics is None and n['state'] == 'modified' and existing:
        changes.append({
            "path": fp,
            "topic": [],
            "subject": [],
            "wiki_role": "wiki",
            "wiki_hash": n['hash'],
            "wiki_indexed": INDEXED,
        })
        preview.append((fp, '(re-stamp only)', [], y.get('topic') or [], []))
        continue

    if topics is None:
        score = Counter()
        for v in (y.get('domain') or []):
            if v in DOMAIN_TOPIC:
                score[DOMAIN_TOPIC[v]] += 2
        for v in (y.get('instrument') or []):
            if v in INSTRUMENT_TOPIC:
                score[INSTRUMENT_TOPIC[v]] += 2
        for v in (y.get('doctrine') or []):
            if v in DOCTRINE_TOPIC:
                score[DOCTRINE_TOPIC[v]] += 1
        for child, par in PARENT.items():
            if child in score and par in score:
                del score[par]
        ranked = [t for t, _ in score.most_common()]
        topics = ranked[:2]
        if 'topic/tokenisation' not in topics and len(topics) < 2:
            topics.append('topic/tokenisation')
        topics = topics[:3]

    org = y.get('organisation') or ''
    subs = [ORG_SUBJECT[org]] if org in ORG_SUBJECT else []

    changes.append({
        "path": fp,
        "topic": topics,
        "subject": subs,
        "wiki_role": "concept" if is_concept else "wiki",
        "wiki_hash": n['hash'],
        "wiki_indexed": INDEXED,
    })
    preview.append((fp, topics, subs, y.get('topic') or [], y.get('domain') or []))

plan = {"vault": VAULT, "changes": changes}
json.dump(plan, open(PLAN_OUT, 'w', encoding='utf-8'), indent=2, ensure_ascii=False)

tc = Counter()
restamp = 0
for c in changes:
    for t in c['topic']:
        tc[t] += 1
    if not c['topic']:
        restamp += 1
print('plan notes:', len(changes), f'({restamp} re-stamp only)')
print('topic freq:', tc.most_common())
print()
print('=== PER-NOTE PREVIEW (plan topics union with existing on apply) ===')
for fp, topics, subs, existing, dom in preview:
    print(fp)
    print(f"    existing: {existing}")
    print(f"    plan add: {topics}  {subs}")
