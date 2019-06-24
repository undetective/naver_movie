import urllib.request
import re
outfile = open("naver_movie.txt","w",-1,"utf-8")
newfile=open("movie_csv.csv","w")
newfile.write("Code,Title,Netizen_rating,Netizen_num,Genre")

file=urllib.request.urlopen("http://movie.naver.com/movie/running/current.nhn")
contents = file.read()
contents = contents.decode("utf-8")
outfile.write(contents)
outfile.close()

outfile = open("naver_movie.txt","r",-1,"utf-8")
for contents in outfile:
    while True:
        try:
            m1 = re.search("""<a href="\/movie\/bi\/mi\/basic\.nhn\?code=([\d]+)">([가-힣\w\s:,.!-]+)<\/a>""", contents)
            code = m1.group(1)
            title = m1.group(2)
            title = title.replace(",","_")
            newfile.write("\n%s," % (code))
            newfile.write("%s," % (title))
            contents.readline()
        except:
            break
    while True:
        try:
            m2 = re.search("""<span class="num">([\d.]+)<\/span><span class="num2">참여 <em>([\d,]+)<\/em>명<\/span>""", contents)
            rating = m2.group(1)
            num = m2.group(2)
            num = num.replace(",", "")
            newfile.write("%s," % (rating))
            newfile.write("%s," % (num))
            contents.readline()
        except:
            break
    while True:
        try:
            m3 = re.search(
                """<a href="\/movie\/sdb\/browsing\/bmovie\.nhn\?genre=([\d]+)">([가-힣\w\/]+)<\/a><!-- N=a:nol.genre,r:([\d]+) -->""", contents)
            genre = m3.group(2)
            newfile.write("%s;" % (genre))
            contents.readline()
        except:
            break


newfile.close()
outfile.close()