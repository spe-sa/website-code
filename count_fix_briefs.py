# from spe_blog.models import Article
from spe_blog.models import Brief
from datetime import datetime
import re
from collections import defaultdict
from django.core.exceptions import ObjectDoesNotExist

d = defaultdict(list)
hits = []
for i in range(0, 2999):
    hits.append(0)
hit_time = []
for i in range(0, 2999):
    hit_time.append(datetime(1970, 1, 1))

with open('../counts/get_merge_log_count.log') as f:
    for line in f:
        columns = line.split('\t')
        if 'briefs-detail' in columns[0]:
            article = re.findall('(art)=(\d+)', columns[0])
            magazine = columns[0][:3]
            if article and article[0][0] == 'art':
                pk = int(article[0][1])
            valid_hits = int(columns[2])
            if valid_hits > 0:
                time = datetime.strptime(columns[5], "%d/%b/%Y:%H:%M:%S\n")
                d[pk].append({magazine, valid_hits, time})
                hits[pk] += valid_hits
                if hit_time[pk] < time:
                    hit_time[pk] = time

y = 0
for i in range(0,2999):
    try:
        art = Brief.objects.get(pk=i)
        # if hits[i]:
        #     print "Updating: ", i, hits[i], art.article_hits, hit_time[i], art.title, "\tRaw: ", d[i]
        # else:
        #     print "Zeroing: ", i, hits[i], art.article_hits, hit_time[i], art.title, "\tRaw: ", d[i]
        art.article_hits = hits[i]
        art.article_last_viewed = hit_time[i]
        art.save()
        y += 1
    except ObjectDoesNotExist:
        if hits[i]:
            print "No Brief Number ", i, hits[i], hit_time[i]
print y, " updated"
