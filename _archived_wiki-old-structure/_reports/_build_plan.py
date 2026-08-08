import json, yaml
from collections import Counter

VAULT = "C:/Users/Simon/Documents/wiki-tokenise"
INDEXED = "2026-06-28T00:00:00Z"

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
    'monetary-policy': 'topic/finance',
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
}

d = json.load(open('_wiki/_reports/scan-2026-06-28.json', encoding='utf-8'))
notes = d['notes']
targets = [n for n in notes
           if n['state'] == 'fresh'
           and n['path'].startswith(('10_Sources', '20_People', '30_Concepts'))
           and not n['path'].endswith('SOURCE-REGISTER.md')]

changes = []
preview = []
for n in targets:
    fp = n['path'].replace('\\', '/')
    txt = open(fp, encoding='utf-8').read()
    y = {}
    if txt.startswith('---'):
        try:
            y = yaml.safe_load(txt.split('---', 2)[1]) or {}
        except Exception:
            y = {}
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
    # suppress a parent when its child is present
    for child, par in PARENT.items():
        if child in score and par in score:
            del score[par]
    ranked = [t for t, _ in score.most_common()]
    topics = ranked[:2]
    if 'topic/tokenisation' not in topics:
        if len(topics) < 2:
            topics.append('topic/tokenisation')
    topics = topics[:3]
    # subjects: publisher only, from whitelist
    org = y.get('organisation') or ''
    subs = []
    if org in ORG_SUBJECT:
        subs = [ORG_SUBJECT[org]]
    changes.append({
        "path": fp,
        "topic": topics,
        "subject": subs,
        "wiki_role": "wiki",
        "wiki_hash": n['hash'],
        "wiki_indexed": INDEXED,
    })
    preview.append((fp, topics, subs,
                    y.get('domain') or [], y.get('instrument') or []))

plan = {"vault": VAULT, "changes": changes}
json.dump(plan, open('_wiki/_reports/apply-plan-2026-06-28.json', 'w', encoding='utf-8'),
          indent=2, ensure_ascii=False)

# distributions
tc = Counter()
ntop = Counter()
nsub = 0
for c in changes:
    ntop[len(c['topic'])] += 1
    for t in c['topic']:
        tc[t] += 1
    if c['subject']:
        nsub += 1
print('plan notes:', len(changes))
print('topics-per-note:', dict(sorted(ntop.items())))
print('notes with publisher subject:', nsub)
print('topic freq:', tc.most_common())
print()
print('=== PER-NOTE PREVIEW ===')
for fp, topics, subs, dom, ins in preview:
    short = fp.split('/', 1)[1]
    print(f"{short}")
    print(f"    -> {topics}  {subs}")
