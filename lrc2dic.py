#-*- encoding: UTF-8 -*-
# reference: (http://reverland.org/python/2014/10/09/lrc/)
#---------------------------------import------------------------------------
import re
#---------------------------------------------------------------------------
def lrc2dict(lrc):
    lrc_dict = {}
    remove = lambda x: x.strip('[|]')
    for line in lrc.split('\n'):
        time_stamps = re.findall(r'\[[^\]]+\]', line)
        if time_stamps:
            # 截取歌词
            lyric = line
            for tplus in time_stamps:
                lyric = lyric.replace(tplus, '')
            # 解析时间
            for tplus in time_stamps:
                t = remove(tplus)
                #print(t)
                tag_flag = t.split(':')[0]
                #print(tag_flag)
                # 跳过: [ar: 逃跑计划]
                if not tag_flag.isdigit():
                    continue
                # 时间累加
                time_lrc = int(tag_flag) * 60
                time_lrc += int(t.split(':')[1].split('.')[0])
                #print(time_lrc)
                lrc_dict[time_lrc] = lyric
    return lrc_dict
############################################################################