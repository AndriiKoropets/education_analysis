#!/usr/bin/env python
# coding: utf-8

# In[19]:


import re
from pathlib import Path
from itertools import accumulate, islice


# In[20]:


german_project_path = Path('/home/ashara/projects/head_first_programming/german_project/')


# In[21]:


get_ipython().system('ls -l {german_project_path}')


# In[22]:


faz_path = german_project_path / 'faz_nordstream.txt'


# In[23]:


all_arts = list()

with faz_path.open('r') as f:
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
                biased = ctype == 'biased'
                art_sents.append(dict(author=author, biased=biased, text=text))
    
    all_arts.append(art_sents)


# In[24]:


sum(len(x) for x in all_arts) == len(comments)


# In[25]:


gen_kw = generate_key_words(key_words)

for kw in gen_kw:
    count = 0
    for art in all_arts:
        for c in art:
            if re.search(kw, c['text'], re.IGNORECASE):
                count += 1
                break
    print(count)


# In[26]:


def load_by_comments():
    comments = list()

    with faz_path.open('r') as f:
        for line in f:
            try:
                author, ctype, text = line.strip().split('>>', 2)
            except ValueError:
                pass
            else:
                biased = ctype == 'biased'
                comments.append(dict(author=author, biased=biased, text=text))
    return comments


# In[27]:


comments = load_by_comments()


# In[28]:


free_context = r'(.{0,200})'
ns2 = r'(Nordstream\s?2|NS\s?2|North\s?Stream\s?2)'
gas = r'(Fracking?-?gas|Flüssig?-?gas|LNG|Fracking|Fragging?-?gas|LPG)'
usa = r'(USA|US|US-Regierung|America|US-Amerikaner|Amerikaner|Ami|Amis)]'

key_words = (
    
      (
        r'zuverl[äa]ssig(er|ste|ere)?',
        fr'{free_context}(Lieferant|Lieferung|Gaslieferant|Energielieferant|Lieferung|)',
        fr'{free_context}Russ?(land|e)'
    ),

       # надійний постачальник газу, партнер
#     fr'{free_context}\b(zuverl[äa]ssig|zuverl[äa]ssiger|zuverl[äa]ssigste|zuverl[äa]ssigere)\b{free_context}\b(Lieferant|Lieferung|Gaslieferant|Energielieferant|Lieferung\b',
    fr'Vertr[äa]ge{free_context}(einhalten|eingehalten|k[üu]ndigen|k[üu]mmern)',
)
print(key_words)


# In[33]:


def generate_key_words(key_words):
    for kw in key_words:
        if isinstance(kw, tuple):
            yield from accumulate(kw)
        else:
            yield kw


# In[34]:


from collections import defaultdict


# In[35]:


key_words_counts = {'biased': defaultdict(int), 'not_biased': defaultdict(int)}
all_blocks = (1, None)
# block_1_inds = (0, 2)

start, end = all_blocks
gen_kw = generate_key_words(key_words[start:end])

for kw in gen_kw:
    count = 0
    for x in comments:
        match = re.search(kw, x['text'], re.IGNORECASE)
        count +=  1 if match else 0
        if x['biased']:
            key_words_counts['biased'][kw] += 1 if match else 0
        else:
            key_words_counts['not_biased'][kw] += 1 if match else 0
            
key_words_counts


# In[36]:


for x in comments:
    print(x)
    break


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[40]:


import re
from pathlib import Path
from itertools import islice, accumulate
from collections import defaultdict

german_project_path = Path('/home/ashara/projects/head_first_programming/german_project/')

faz_path = german_project_path / 'faz_nordstream.txt'

all_arts = list()

with faz_path.open('r') as f:
    next(f)

    art_sents = list()
    for line in f:
        if '>  > NAME' in line:
            all_arts.append(all_sents)
            art_sents = list()
        else:
            try:
                author, ctype, text = line.strip().split('>>', 2)
            except ValueError:
                pass
            else:
                biased = ctype = 'biased'
                art_sents.append(dict(author=author, biased=biased, text=text))
    all_arts.append(art_sents)

free_context = r'(.{0,200})'
ns2 = r'(Nordstream\s?2|NS\s?2|North\s?Stream\s?2)'
gas = r'(Fracking?-?gas|Flüssig?-?gas|LNG|Fracking|Fragging?-?gas|LPG)'
usa = r'(USA|US|US-Regierung|America|US-Amerikaner|Amerikaner|Ami|Amis)]'

key_words = (

    (
        r'zuverl[äa]ssig(er|ste|ere)?',
        fr'{free_context}(Lieferant|Lieferung|Gaslieferant|Energielieferant|Lieferung|)',
        fr'{free_context}Russ?(land|e)'
    ),

    # надійний постачальник газу, партнер
    #     fr'{free_context}\b(zuverl[äa]ssig|zuverl[äa]ssiger|zuverl[äa]ssigste|zuverl[äa]ssigere)\b{free_context}\b(Lieferant|Lieferung|Gaslieferant|Energielieferant|Lieferung\b',
    fr'Vertr[äa]ge{free_context}(einhalten|eingehalten|k[üu]ndigen|k[üu]mmern)',
    fr'\b(Russland|Russen)?\b{free_context}\b(zuverl[äa]ssig|zuverl[äa]ssiger|zuverl[äa]ssigste|zuverl[äa]ssigere)\b{free_context}\b(Lieferant|Lieferung|Gaslieferant|Energielieferant|Lieferung|)\b',
)


# print(key_words)

def generate_key_words(key_words):
    for kw in key_words:
        if isinstance(kw, tuple):
            yield from accumulate(kw)
        else:
            yield kw


gen_kw = generate_key_words(key_words)
for kw in gen_kw:
    # print(kw)
    count = 0
    for art in all_arts:
        for c in art:
            if re.search(kw, c['text'], re.IGNORECASE):
                count += 1
                break

    # print(count)


def load_by_comments():
    comments = list()

    with faz_path.open('r') as f:
        for line in f:
            try:
                author, ctype, text = line.strip().split('>>', 2)
            except ValueError:
                pass
            else:
                comments.append(dict(author=author, biased=ctype, text=text))
    # print(comments)
    return comments


key_words_counts = {'biased': defaultdict(int), 'not_biased': defaultdict(int)}
all_blocks = (1, None)
# block_1_inds = (0, 2)

start, end = all_blocks
gen_kw = generate_key_words(key_words[start:end])

# print(len(comments))

count_biased = 0
count_not_biased = 0
# print(comments)
#     count = 0

all_comments = load_by_comments()
# print(all_comments)
# print(list(gen_kw))
# for x in all_comments:
#     if x['biased'] == 'biased':
#         count_biased += 1
#         # print(list(gen_kw))
#         print(gen_kw)
#         for kw in gen_kw:
#             print("aaaaaaaaaaaaaaaaaaaaaaa")
#             count_biased += 1
#             match = re.search(kw, x['text'], re.IGNORECASE)
#             print("match = " + match)
#             if match:
#                 print("here")
#                 key_words_counts['biased'][kw] += 1
#             else:
#                 key_words_counts['not_biased'][kw] += 1
#     else:
#         count_not_biased += 1

for kw in gen_kw:
    for x in all_comments:
        match = re.search(kw, x['text'], re.IGNORECASE)
        # print(x)
        # print(x['biased'])
        # print(x['biased'] == 'biased')
        if x['biased'] == 'biased' :
            # print("here")
            key_words_counts['biased'][kw] += 1 if match else 0
        else:
#             print('here')
            key_words_counts['not_biased'][kw] += 1 if match else 0


print("biased = " + str(count_biased))
print("not_biased = " + str(count_not_biased))
print("Keywords = " + str(key_words_counts['biased']))
print("Keywords = " + str(key_words_counts['not_biased']))


key_words_counts


# In[ ]:




