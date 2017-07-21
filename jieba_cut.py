import pickle
import jieba
import progressbar
import csv


def jieba_cut(boardname, filename):
    bar = progressbar.ProgressBar(max_value=progressbar.UnknownLength)
    ptt = pickle.load(open("/home/ptt/ptt_{}_{}.txt".format(boardname, filename), "rb"))
    jieba.load_userdict("for_jieba_seasoning.txt")


    total_page = len(ptt)
    start = 0
    end = 20000

    page_count = 0

    while True:
        for content in ptt[start:end]:
            seg_list = list(jieba.cut(content[-1], cut_all=False))
            content.append(seg_list)
            page_count += 1
            bar.update(page_count)

        pickle.dump(ptt, open("ptt_{}_text_jieba_pickle.txt".format(boardname), "wb"))

        f = open('ptt_{}_text_jieba.csv'.format(boardname), 'w')
        w = csv.writer(f)
        w.writerows(ptt)
        f.close()

        if end == total_page:
            break

        start += 20000
        end += 20000
        if end > total_page:
            end = total_page

        ptt = pickle.load(open("ptt_{}_text_jieba_pickle.txt".format(boardname), "rb"))
