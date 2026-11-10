"""Writes repo/README.md and repo/jurisdiction.json for corpus.json plus every signed-off corpus.d part (General
Statutes chapters read from the newest Internet Archive capture of each chapter page). No network.
    python -X utf8 docs_ia.py
"""
import json, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
R = os.path.join(HERE, 'repo')
NL = '\n'


def key(x):
    return [int(y) if y.isdigit() else y for y in re.split(r'(\d+)', x)]


parts = sorted((f for f in os.listdir(os.path.join(HERE, 'corpus.d')) if f.endswith('.json')
                and os.path.exists(os.path.join(HERE, 'corpus.d', f[:-5] + '.PUBLISH'))), key=key)
new = [json.load(open(os.path.join(HERE, 'corpus.d', f), encoding='utf-8'))['acts'][0] for f in parts]
new.sort(key=lambda a: key(a['slug']))
rows = NL.join(f"| `{a['slug']}/` | {a['title']} | 1 | {len(a['versions'][0]['units'])} sections; capture of {a['versions'][0]['from']} |" for a in new)
nsec = sum(len(a['versions'][0]['units']) for a in new)

t = open(os.path.join(R, 'README.md'), encoding='utf-8').read()
t = re.sub(r'\n\| `chapter-(?!14/|55/|42/)[^\n]*', '', t)
i = t.index('| `chapter-42/` |')
j = t.index(NL, i)
t = t[:j] + (NL + rows if rows else '') + t[j:]
t = re.sub(r'Nothing else of North Carolina\'s law is in it yet\.|In all: [^\n]*',
           f'In all: the Constitution and {len(new) + 3} chapters of the General Statutes. The other chapters are not in it yet.', t)
t = re.sub(r'\[North Carolina General Assembly: Constitution and General Statutes\]\(https://www\.ncleg\.gov/Laws/GeneralStatutes\)\. [^\n]*?(Only section headings)',
           r'\1', t)
t = re.sub(r'Only section headings and text are taken; the history notes in brackets are left out\.[^\n]*',
           'Only section headings and text are taken; the history notes in brackets at the end of a section are left out where their form is recognised (some older ones, such as those citing C.C.P., stay). Every text is an Internet Archive '
           'capture of the General Assembly\'s own public page (ncleg.gov).', t)
dates_new = ('- Chapters added on 2026-11-10 hold one version each: the newest Internet Archive capture of the chapter page, dated by '
             'the capture day (the page states no currency date). Their sections\' structural headings (Subchapter, Article, Part) are '
             'not part of any section, and a heading such as "2-1 through 2-60" keeps its whole range.')
t = re.sub(r'\n- Chapters added on 2026-11-10[^\n]*', '', t)
k = t.index('## What it does not show')
t = t[:k].rstrip(NL) + NL + NL + dates_new + NL + NL + t[k:]
t = re.sub(r'- Only the Constitution and chapters 14, 42 and 55 are included\.|- Only the Constitution and [^\n]*chapters are included[^\n]*',
           f'- Only the Constitution and {len(new) + 3} chapters are included; a chapter whose page the Internet Archive does not hold is not.', t)
open(os.path.join(R, 'README.md'), 'w', encoding='utf-8', newline=NL).write(t)

jp = os.path.join(R, 'jurisdiction.json')
j = json.load(open(jp, encoding='utf-8'))
j['build'] = f'built: Constitution and {len(new) + 3} General Statutes chapters ({nsec} sections in the {len(new)} added 2026-11-10), from Internet Archive captures'
open(jp, 'w', encoding='utf-8', newline=NL).write(json.dumps(j, ensure_ascii=False, indent=2) + NL)
print(len(new), 'added chapters,', nsec, 'sections')
