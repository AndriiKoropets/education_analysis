#!/usr/bin/env python
# coding: utf-8

# In[22]:


import re
from pathlib import Path
from itertools import accumulate, islice


# In[23]:


german_project_path = Path('/home/ashara/projects/head_first_programming/german_project/')


# In[24]:


get_ipython().system('ls -l {german_project_path}')


# In[25]:


welt_path = german_project_path / 'welt_nordstream.txt'


# In[26]:


all_arts = list()

with welt_path.open('r') as f:
    next(f)
    
    art_sents = list()
    for line in f:
        if '>> NAME' in line:
            all_arts.append(art_sents)
            art_sents = list()
        else:
            try:
                author, ctype, text = line.strip().split('>>', 2)
            except ValueError:
                pass
            else:
                trolling = ctype == 'trolling'
                art_sents.append(dict(author=author, trolling=trolling, text=text))
    
    all_arts.append(art_sents)


# In[27]:


sum(len(x) for x in all_arts) == len(comments)


# In[28]:


gen_kw = generate_key_words(key_words)

for kw in gen_kw:
    count = 0
    for art in all_arts:
        for c in art:
            if re.search(kw, c['text'], re.IGNORECASE):
                count += 1
                break
    print(count)


# In[29]:


def load_by_comments():
    comments = list()

    with welt_path.open('r') as f:
        for line in f:
            try:
                author, ctype, text = line.strip().split('>>', 2)
            except ValueError:
                pass
            else:
                trolling = ctype == 'trolling'
                comments.append(dict(author=author, trolling=trolling, text=text))
    return comments


# In[30]:


comments = load_by_comments()


# In[31]:


free_context = r'(.{0,200})'
ns2 = r'(Nordstream\s?2|NS\s?2|North\s?Stream\s?2|Nordstream 2|Nord Stream 2|Pipeline)'
gas = r'(Fracking?-?gas|Flüssig?-?gas|LNG|Fracking|Fragging?-?gas|LPG|US-Fraking Gas|Fracking Gas|Gas|Frackinggas|Fracking-Gas)'
usa = r'(USA|US|US-Regierung|America|US-Amerikaner|Amerikaner|Ami|Amis|Trump|Donald Trump|Washington)'

key_words = (
    
    # надійний постачальник газу, партнер
    (
        r'zuverl[äa]ssig(er|ste|ere)?',
        fr'{free_context}(Lieferant|Lieferung|Gaslieferant|Energielieferant|Lieferung|)',
        fr'{free_context}Russ?(land|e)'
    ),
#     fr'\b(Russland|Russen)?\b{free_context}\b(zuverl[äa]ssig|zuverl[äa]ssiger|zuverl[äa]ssigste|zuverl[äa]ssigere)\b{free_context}\b(Lieferant|Lieferung|Gaslieferant|Energielieferant|Lieferung|)\b',
#     fr'\b(zuverl[äa]ssig|zuverl[äa]ssiger|zuverl[äa]ssigste|zuverl[äa]ssigere)\b{free_context}\b(Lieferant|Lieferung|Gaslieferant|Energielieferant|Lieferung)\b{free_context}\b(Russland|Russen)\b',
#     fr'\bRuss?enhass\b',
#     fr'gegen Russ?land',
#     fr'\b(Russland|Russen)?\b{free_context}\b(Vertrag|Vertr[äa]ge)\b{free_context}(einhalten|eingehalten|k[üu]ndigen|k[üu]mmert|erhalten)',
#     fr'\b(Russland|Russen)?\b{free_context}\b(Vertragstreue|vertragstreu(er)?|liefertreu|Vertragserfüllung)\b',
#     fr'\b(Russland|Russen)\b{free_context}\b(verl[äa]sslich|verl[äa]sslicher|zuverl[äa]ssiger)\b{free_context}\b(|Handelspartner|Gesch[äa]ftspartner)\b',
#     fr'\b(Russland|Russen)?\b{free_context}\b(Gaslieferung|Gaslieferungsvertrag|Gaslieferungen|Gaslieferungs-Vertrag|Lieferungsverpflichtungen|Verpflichtungen){free_context}(erfüllt|gehalten|einhalten|eingehalten)',
#     fr'\b(Russland|Russen)\b{free_context}\b(Freund|Partner|Vertragspartner)\b',
#     fr'\b(Russland|Russen)?\b{free_context}\bzuverlässig\b{free_context}\b(geliefert|liefert|belifert)\b',
#     fr'\b(Russland|Russen|Putin)\b{free_context}\bnie\b{free_context}|b(Lieferung|Gaslieferung)\b{free_context}\bgestoppt\b',
#     fr'\b(Russ?isch|Russ?isches)\b{free_context}\b(Gas|gas|Erdgas)\b{free_context}\b(g[üu]nstig|g[üu]nstiger)\b',
#     fr'\b(Russland|Russen|UdSSR)\b{free_context}\b(kalten Krieg|in schlimmsten Zeiten|in Zeiten des kältesten Krieges)\b',
    
#     # Північний потік - це найкраще рішення для Європи
#     fr'{ns2}{free_context}\b(Interessen|notwendig)\b',
#     fr'{usa}{free_context}\bgegen\b{free_context}{ns2}',
#     fr'{ns2}{free_context}verhindern',
#     fr'{ns2}{free_context}\b(richtig|gut|super|nötig|notwendig|wichtig)\b',
#     fr'{ns2}{free_context}\bVorteil\b',
#     fr'{ns2}{free_context}\b(unserem|unsere|deutschen|europäischen)\b{free_context}\b(Interesse|Interessen)\b',
#     fr'{ns2}{free_context}\bFriedensprojekt\b',
    
    # США тиснуть на Німеччину бо хочуть продавати свій сланцевий газ
#     fr'{gas}{free_context}\b(verkaufen|kaufen)\b',
#     fr'{gas}{free_context}\b(umweltschädliche?|umweltbelastend|umweltfeindliche|schmutziges)\b',
#     fr'\b(umweltschädliche?|umweltbelastend|umweltfeindliche|schmutziges)\b{free_context}{gas}',
#     fr'{gas}{free_context}\bUSA\b{free_context}\bimportieren\b', 
#     fr'\b(Abhängigkeit|abhängig)\b{free_context}{usa}',
#     fr'{usa}{free_context}\b(Abhängigkeit|abhängig)\b',
#     fr'\Deutschland First',
#     fr'\bAmerica First\b',
#     fr'{usa}{free_context}\b(erpressen|erpresst|Erpressung|einmischt|Einmischung|bedrohen|bedroht|drohen|droht)\b',
#     fr'\b(erpressen|erpresst|Erpressung|einmischt|Einmischung|bedrohen|bedroht|drohen|droht)\b{free_context}{usa}',   
#     fr'{usa}{free_context}\bwirtschaftlichen\b{free_context}\bInteressen\b',
#     fr'{usa}{free_context}\bvertreten\b{free_context}\bInteressen\b',
#     fr'{usa}{free_context}\b(EU|Europa)\b{free_context}\b(spalten|gespaltet)\b', 
#     fr'\bkeine\b{free_context}\bdeutschen\b{free_context}\bInteressen\b',
#     fr'{usa}{free_context}\b(drücken|drückt|gedrückt)\b',
#     fr'{usa}{free_context}\bGeschäfte\b{free_context}\bmachen\b',   
#     fr'{usa}{free_context}\bgegen\b{free_context}\bDeutschland\b',
#     fr'{usa}{free_context}\bgegen\b{free_context}\b(Russland|Russen|Putin)\b',
#     fr'\bKolonialmacht\b',      
#     fr'{usa}{free_context}\b(EU|Europa|Europäische union)\b{free_context}\b(zerstören|zerstört)\b',
#     fr'{usa}{free_context}\bGefahr\b{free_context}\b(EU|Europa|Europäische union)\b',
#     fr'{usa}{free_context}\bDeutschland\b{free_context}\b(isolieren|isoliert)\b',fr'{usa}{free_context}\b(drohen|droht|Drohungen|Drohung|bedroht|Drohbriefe,angedroht,gedroht,drohende, Bedrohungen, Androhung)\b',
#     fr'{usa}\b{free_context}\b(teuer|teurer)\b{free_context}{gas}',
#     fr'\bVerbündeten\b',
#     fr'\bDruck\b{free_context}{usa}',
#     fr'{usa}{free_context}\bDruck]b',
    
#     # Україна не надійний постачальник газу, країна - банкрот 
#     fr'\bKorruption\b{free_context}\b(Ukraine|Kiew)\b',
#     fr'\bUkraine\b{free_context}\bPleite\b',
#     fr'\bUkraine\b{free_context}\bInteressen\b{free_context}\bvertreten\b',
#     fr'\b(Oligarchen|ukrainische Oligarchen|Schokoladen Prinz|Gasprinzessin)\b',
#     fr'\b(Erpressung|erpressen)\b{free_context}\b(Ukraine|Kiew)\b',
#     fr'\b(Ukraine|Kiew)\b{free_context}\b(Erpressung|erpressen|erpresst)\b',
#     fr'\b(Ukraine|Kiew)\b{free_context}\b(drohen|droht|Drohungen|Drohung|bedroht|Drohbriefe,angedroht,gedroht,drohende, Bedrohungen, Androhung)\b',
#     fr'\b(drohen|droht|Drohungen|Drohung|bedroht|Drohbriefe,angedroht,gedroht,drohende, Bedrohungen, Androhung)\b{free_context}\b(Ukraine|Kiew)\b',    
#     fr'\bKrim\b{free_context}\b(gehörte|gehört|ist|war)\b{free_context}\b(Russland|russisch)',
#     fr'\bUkraine\b{free_context}\b(Bürgerkrieg|Bürgerkriegsgebiet)\b', 
#     fr'\bPutsch\b{free_context}\b(Kiew|Ukraine)\b',    
#     fr'\b(Abhängigkeit|Abhängig|abhängig)\b{free_context}\b(Ukraine|Kiew)\b',
#     fr'\b(Ukraine|Kiew)\b{free_context}\b(Abhängigkeit|Abhängig|abhängig)\b',
#     fr'\b(Unabhängigkeit|unabhängig)\b{free_context}\b(Ukraine|Kiew)\b',
#     fr'\b(Ukraine|Kiew)\b{free_context}\b(Unabhängigkeit|unabhängig)\b',    
#     fr'\b(Ukraine|Kiew)\b{free_context}\b(kassiert|abkassiert)\b',
#     fr'\b(Kiew|Ukraine)\b{free_context}\b(geklaut|abzapfte|abzapft|abgezapft|beklaut)\b',
#     fr'\b(Kiew|Ukraine)\b{free_context}\b{gas}\b{free_context}\bgestohlen\b',
#     fr'\bUkraine\b{free_context}\bnicht\b{free_context}\bbezahlt\b',
#     fr'\balte\b{free_context}\bPipeline\b',
#     fr'\b(Kiew|Ukraine)\b{free_context}\b(kaufen|gekauft)\b{free_context}{gas}',
#     fr'\b(Kiew|Ukraine)\b{free_context}\bgegen\b{free_context}{ns2}',   
#     fr'\b(Kiew|Ukraine)\b{free_context}\b(verliert|verliere)\b{free_context}\bTransitgebühren\b',  
#     fr'\b(Kiew|Ukraine)\b{free_context}\bsubventionieren',

#     # НАТО
#     fr'\bNATO\b{free_context}\bausweiten\b',
#     fr'\brussischen\b{free_context}\bGrenze\b{free_context}\bWaffensysteme\b',
#     fr'\b(Nato|NATO)\b{free_context}\bOsterweiterung\b',
#     fr'\bStationierung\b{free_context}\b(US Truppen|amerikanischer Soldaten)\b',
    
#     # Транзитні заробітки
    
#     fr'\bTransitgebühren\b{free_context}\b(abschneiden|abzuschneiden|abkassieren|abkassiert|kassieren|kassiert|entfallen|wegfallen|wegfielen|angefallen|fällig wären|abgreifen|pampern|Zahlen|einstecken|verschwinden|bezogen|schnorren|speisen|nicht mehr bekommen|schwimmen|hätten|auf unsere Kosten|alimentieren|verdienen|verdient|unterbinden|verlieren|verliert|verloren|verlangen|protegieren|kommen bestimmt nicht|befreien|bekommen|abzudrücken|finanzieren|einstreichen|fehlen|subventionieren|hoffen|erhalten)\b',    
#     fr'\b(abschneiden|abzuschneiden|abkassieren|abkassiert|kassieren|kassiert|entfallen|wegfallen|wegfielen|angefallen|fällig wären|abgreifen|pampern|Zahlen|einstecken|verschwinden|bezogen|schnorren|speisen|nicht mehr bekommen|schwimmen|hätten|auf unsere Kosten|alimentieren|verdienen|verdient|unterbinden|verlieren|verliert|verloren|verlangen|protegieren|kommen bestimmt nicht|befreien|bekommen|abzudrücken|finanzieren|einstreichen|fehlen|subventionieren|hoffen|erhalten)\b{free_context}\bTransitgebühren\b',    
#     fr'\bDurchleitungsgebühren\b{free_context}\b(abschneiden|abzuschneiden|abkassieren|abkassiert|kassieren|kassiert|entfallen|wegfallen|wegfielen|angefallen|fällig wären|abgreifen|pampern|Zahlen|einstecken|verschwinden|bezogen|schnorren|speisen|nicht mehr bekommen|schwimmen|hätten|auf unsere Kosten|alimentieren|verdienen|verdient|unterbinden|verlieren|verliert|verloren|verlangen|protegieren|kommen bestimmt nicht|befreien|bekommen|abzudrücken|finanzieren|einstreichen|fehlen|subventionieren|hoffen|erhalten)\b',    
#     fr'\b(abschneiden|abzuschneiden|abkassieren|abkassiert|kassieren|kassiert|entfallen|wegfallen|wegfielen|angefallen|fällig wären|abgreifen|pampern|Zahlen|einstecken|verschwinden|bezogen|schnorren|speisen|nicht mehr bekommen|schwimmen|hätten|auf unsere Kosten|alimentieren|verdienen|verdient|unterbinden|verlieren|verliert|verloren|verlangen|protegieren|kommen bestimmt nicht|befreien|bekommen|abzudrücken|finanzieren|einstreichen|fehlen|subventionieren|hoffen|erhalten)\b{free_context}\bDurchleitungsgebühren\b',    
#     fr'\bohne\b{free_context}\b(Umweg|Umwege)\b',
#     fr'\b(gas|Gas)\b{free_context}\bdirekt\b', 
   
    fr'\bDurchleitungsgebühren\b{free_context}\b(abschneiden|abzuschneiden|erhalten|befreien|eingeschränkt|sparen)\b', 
    fr'\b(Durchleitungsgebühre|Durchleitungsgebühren)\b{free_context}\b(kassiert|kassieren|kassierten)\b',
    fr'\b(Ukraine|Polen)\b{free_context}\bverdienen\b',
    
    # Gruenen
#     fr'\bGrünen\b{free_context}{gas}',
#     fr'\bGrünen\b{free_context}\bTransatlantiker\b',
#     fr'\bGrünen\b{free_context}\b(gegen|Gegner)\b{free_context}{ns2}', 
#     fr'\bGrünen\b{free_context}\bgegen\b{free_context}\bDeutschland\b',
#     fr'\bGrünen\b{free_context}\bkeine\b{free_context}\bFreunde\b', 
#     fr'\bGrünen\b{free_context}\b(Populismus|Populisten)\b',
#     fr'\bGrünen\b{free_context}\bKatastrophe\b', 
#     fr'\bGrünen\b{free_context}\bdeindustrialisieren\b',

)


# In[32]:


def generate_key_words(key_words):
    for kw in key_words:
        if isinstance(kw, tuple):
            yield from accumulate(kw)
        else:
            yield kw    


# In[33]:


from collections import defaultdict


# In[38]:


key_words_counts = {'trolling': defaultdict(int), 'not_trolling': defaultdict(int)}

all_blocks = (1, None)
block_1_inds = (0, 12)
block_2_inds = (12, 21)
block_3_inds = (21, None)

start, end = all_blocks
gen_kw = generate_key_words(key_words[start: end])
# print(gen_kw)

# for kw in ['Trump', 'Putin', r'Porosc?henko']:
for kw in gen_kw:    
#     print(kw)
    count = 0
    for x in comments:
        match = re.search(kw, x['text'], re.IGNORECASE)
        count += 1 if match else 0
        print(x)
        print(x['trolling'])
        if x['trolling']:
            key_words_counts['trolling'][kw] += 1 if match else 0
        else:
#             print('here')
            key_words_counts['not_trolling'][kw] += 1 if match else 0
            
#     key_words_counts[kw] = count
    

key_words_counts


# In[81]:


# sum(key_words_counts.values())


# In[16]:


for x in comments:
    print(x)
    break


# In[255]:


# (sum(list(key_words_counts.values())[1:]) - 30) / len(comments)


# In[658]:


# Trump counter

trump_counter = 0

if 'Trump' in trolling:
    trump_counter += 1
else:
    print('Fickt euch')


# In[654]:


for i in [1, 2, 3, 4][::-1]: 
    print (i)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




