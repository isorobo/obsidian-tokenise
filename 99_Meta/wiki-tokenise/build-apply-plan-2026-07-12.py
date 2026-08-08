# Build apply-plan for the 2026-07-12 wiki-refresh.
# Adapted from _archived_wiki-old-structure/_reports/_build_plan.py for the
# restructured vault: scan JSON lives in 99_Meta/wiki-tokenise/, synthesis
# notes live in 30_Areas/ (classified via OVERRIDES), and modified notes that
# already carry topics get a hash re-stamp only.
import json
from collections import Counter

import yaml

VAULT = "C:/Users/Simon/Documents/wiki-tokenise"
SCAN = VAULT + "/99_Meta/wiki-tokenise/wiki-scan-2026-07-12.json"
PLAN_OUT = VAULT + "/99_Meta/wiki-tokenise/apply-plan-2026-07-12.json"
INDEXED = "2026-07-12T00:00:00Z"

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
}
QUARANTINE = ['AWS-Bedrock-AgentCore-Payments.md']  # empty stub, unclassifiable

d = json.load(open(SCAN, encoding='utf-8'))
notes = d['notes']
targets = [n for n in notes
           if n['state'] in ('fresh', 'modified')
           and n['path'].replace('\\', '/').startswith(('10_Sources', '30_Areas'))
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

    # Modified note that already carries topics: re-stamp hash only.
    if n['state'] == 'modified' and (y.get('topic') or []):
        changes.append({
            "path": fp,
            "topic": [],
            "subject": [],
            "wiki_role": "wiki",
            "wiki_hash": n['hash'],
            "wiki_indexed": INDEXED,
        })
        preview.append((fp, '(re-stamp only)', [], [], []))
        continue

    topics = None
    for key, override in OVERRIDES.items():
        if key in fp:
            topics = list(override)
            break
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
        "wiki_role": "wiki",
        "wiki_hash": n['hash'],
        "wiki_indexed": INDEXED,
    })
    preview.append((fp, topics, subs, y.get('domain') or [], y.get('instrument') or []))

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
print('=== PER-NOTE PREVIEW ===')
for fp, topics, subs, dom, ins in preview:
    print(fp)
    print(f"    -> {topics}  {subs}")
