# Web
## SQLI 30

Author: maritio_o

Have you heard about input validation? Do you validate you input in your systems? You see.. I need some help.. I got an anonymous tips that my site is vulnerable to something called an SQL injection. I have no idea what that is. Can you help me?

I do not do any input validation as of now. This is a snippet from my SQL query:


    sql_query = "SELECT * from users WHERE username = '" + username + 
	"' and password = '" + md5(password) + "';";
And here is my web page:

sqli1.datasnok.no

### Hints
You may read about SQL injections and how to prevent SQL injections in your own code here. For detailed information about SQL Injection exploiting, read the sections 'SQL Injections', 'How SQL Works' and 'Hacking Web Pages using SQL' from TG:Hack 2018's tutorial page.

## 'C' is for "Cookies" 50

Author: maritio_o

https://www.youtube.com/watch?v=Ye8mB6VsUHw "That's good for me!"

This is the task:

cookiemonster.datasnok.no

### Hints

Take a look in this page , or the this Wikipedia page that also mentions security issues!

## Hidden in plain sight 75

Author: maritio_o

So hidden.

plainsight.datasnok.no

### Hints 
All web pages are hosted in a file structure, just like in the Windows File explorer. Although not common nowadays, some pages may allow traversing through the web server directories through input fields. Can you do it? ;)
Remember the flag format always have upper case S in SopraSteria{}

## Super Awesome Web Project 200

    Hey everyone..

    I got an angry note from the security team in my super awesome web project. She sent me the following email:

    Hi, maritio_o.... 

    Secrets should NEVER EVER be pushed to git. 
    Please, in the future ONLY keep the secrets locally on your machine.
    Or, you may as well store your secrets in a tool like a key vault. 

    Just keep it away from our public repository!!! You should be more careful!!

    Regards,
    Security Expert Lady

I deleted the secret to generate access tokens withing the API ages ago.. I can't seem to find anything bad in my code and in our repository... Can you?

You may find our super awesome project repository here. https://github.com/maritiren/superawesomeproject

NOTE! If you see tghack.no anywhere, replace it with datasnok.no

Btw. Use https, not http.

## Keep your secrets safe.. 250

This web API might have been rushed to production.. Can you see why?

Many of the current systems use Swagger to document their API's. This system does as well, and all the information you'll need to enter the API is here:

https://api.datasnok.no/api-docs

### Hints 
When solving this task, we strongly recommend using Postman. Other tools and topics worth searching for:

* Json Web Token, also called jwt.
* This blogpost about Understanding HTTP Basics.
* This Youtube video to get familiar with Postman.
* This page containing information about HTTP requests and loads tips and tricks for different kinds of HTTP requests.
* #It might be a good idea to read the documentation, and check required authorization.

# Misc

## If i only knew 10

If I only knew where to get more information about the Graduate Program...

## Zipper 75

Something got stuck in the zipper, lets hope it wasn't in the fly.

//Check folder zipper

## Exciting 100
Numbers are numbers and letters are letters, or are they? Anyways, here are some numbers for Sopra Steria.


//check folder exciting

## T-2000 100

Try to get through this manuscript, it's supposed to be another blockbuster.

By the time you get to the end of the manuscript, make sure to remember that he couldn't count to more than 8 before he had to start over.

### Note
This task may have some trouble showing the curlybrackets correct. But you will know when you find the flag.
// check folder t-2000

## Hack through time and space 100

Hackerman is somewhere on the spectre, am i right?

Listen to this tutorial on how to hack through time and space.


## Evilcorp's Coffee 250

I recently hacked a corporation. Dont't worry; I know they're evil. They use Java. I have acquired an encrypted password - `i_o_4hr4_l4hrk_lc4hl4rutsgd_rs4_rh_` - and I am almost positive this is what you are looking for, but I can't seem to decrypt it... I also managed to get some of their code (their terrible, evil code), and a property file. Maybe you can figure it out?

* config.properties https://datasnok.no/files/0e074f9547bfe4dc2023b1d51238ed46/config.properties
* SecurityManagerImpl.java.txt https://datasnok.no/files/52c1b4012134a7f566b5ae0d4066c3f5/SecurityManagerImpl.java.txt

### Tips

There is a lot of code that doesn't seem to do anything useful... Lots of information that doesn't mean anything... And some deceptive naming practices.
Regular expressions are a pain to get right.
Formatting... Not that important, right?
It's also good to know when to take a break;

# Pwn

## Sopra Steria's Super Secret Storage 100

I found this on my boss' computer, can you help me fetch some files?

nc buffer.datasnok.no 4000
You can find the source code in the .c file below.

### Note

* You may only solve the pwn tasks using a terminal on a Linux distribution (Linux environment on Windows or the terminal on Mac will not work).
* This is a 32 bit binary, which means your Linux distro needs special packages installed. Take a look at this page for help.
* You are not supposed to compile the source code, it is only given to you to read and understand the program.
* Make the binary file executable on you machine by using the command chmod +x secret_storage. Then you may run it using the command ./secret_storage.

### Guide for solving this binary exploitation task

* Read and analyze the source code (secret_storage.c) to find the vulnerability.
* When you think you know the vulnerability in the code, you should run the executable (secret_storage) locally on your machine using a debugger to get knowledge of the stack in order to manipulate it to paste the flag.
* To actually get the flag, you must send your input to the server using netcat.
* Need more detailed help? Read TG:Hack 2019's tutorial on binary exploitation. https://tghack.no/page/Pwntions%20tutorial

## Format String 150

    My colleague told me my program is buggy. I can't find anything, can you?

    nc format.datasnok.no 5000

Download the binary file format to test the task locally. However, this only contain a placeholder flag, so you need to connect to our server using netcat in the terminal as shown above.

Hint: read this https://resources.infosecinstitute.com/format-string-bug-exploration/#gref

### Note 
* Make the binary file executable with the command chmod +x format. Then you may run it using the command ./format

## Ping Pong 200

To play the ping game, please log in here:

nc heap.datasnok.no 6000

### Hint: 

Google "use after free" and checkout this github page. https://github.com/shellphish/how2heap/blob/master/first_fit.c

## ROP32 250

    Can you rop me?

    nc rop32.datasnok.no 7000
    Here, take this binary file to do some research on your own.

Libc-version: Ubuntu GLIBC 2.23-0ubuntu11 Download libc versions using this tool: https://github.com/niklasb/libc-database

# Forensics

## Another Selfie 100

My selfie got stuck in transmission. I hope no one finds it, its quite an embarassing one.

Here is what I got:

## Mona lisas secret 100

Look at that smile, she must be hiding something.

Probably the least significant secret I've ever seen, though.

## we need to agree 150

We both agree, this is a secure transmission right?

### Hint

Use Wireshark to inspect the traffic.

Use the python code to decrypt.

## Parallel universe 150
A Windows-expert has hidden some secrets in a file, can you figure out where the flag is hidden?

`this:is:my:data`

### Tips

You should investigate this case using your favorite operating system: Windows.

# Crypto

## The sopra steria history 30
Here's Sopra Steria's history. It isn't as messy as it looks..

    Xyijehyud ec Iefhq Ijuhyq
    2015 - Iubiaqfuj udthuh dqld jyb Iefhq Ijuhyq
    2014 - Ijuhyq vkizeduhuh cut tuj vhqdiau aedikbudjiubiaqfuj Iefhq
    Xyijehyud ec Ijuhyq
    2008 – Fqiiuhuh 20 000 cutqhruytuhu.
    2007 – Azøfuh tuj rhyjyiau ekjiekhsydwiiubiaqfuj Nqdiq, ew xqh ujjuh effazøfuj 18 000 cutqhruytuhu y 16 bqdt. Tuhyrbqdj 5000 y Ydtyq.
    2006 – Fqiiuhuh 10 000 cutqhruytuhu.
    2005 – Ujqrbuhydw ql Ijuhyq-aedjeh y Febud. Effazøf ql Ckccuhj Sedikbjydw y Joiabqdt.
    2004 – SYS-iuskhyjyui aåhuh Ijuhyq jyb Ukhefqi ruiju yj-aedikbudjiubiaqf veh qdthu åhuj få hqt. Ujqrbuhydw ql Ijuhyq-aedjeh y Xedwaedw.
    2003 – SYS-iuskhyjyui aåhuh Ijuhyq jyb Ukhefqi ruiju yj-aedikbudjiubiaqf.
    2002 – Fqiiuhuh 1 cybbyqht ukhe y eciujdydw.
    2001 – Azøfuh Rkbbi ukhefuyiau aedikbudjtylyized Ydjuwhyi.
    2000 – Yddwåh aedjhqaj cut Suwujub, XF ew ZT Utmqhti veh å jybro ed-bydu QIF-jzuduijuh. Azøfuh Unfuhyqdi ekjiekhsydwilyhaiecxuj Vkized cut JUSIY. Azøfuh UGKYF whkffud.
    1999 – Ujqrbuhuh uj tqjjuhiubiaqf iqccud cut Qjei yddud dujjrqdaioijucuh. Ujqrbuhuh tqjjuhiubiaqfudu Ijuhyq KA ew Ijuhyq Qiyq y Iydwqfehu. Åfduh uj aedjeh y Tüiiubtehv, Joiabqdt. Dejuhui få Iusedt Cqhsxé få røhiud y Fqhyi.
    1998 – Vhqdseyi Udqkt kjduldui jyb ijohubutuh ew aediuhdizuv.
    1994 – Kjlyabuh uj ijohydwiioijuc veh rujqbydw cubbec rqdauh "Sudjhqbu tui Héwbucudji Ydjuhrqdsqyhui".
    1993 - Ycfbucudjuhuh ydvehcqizediioijucuj få Zqaqhjqi vbofbqii.
    1990 – Ujqrbuhuh tqjjuhiubiaqf ew aedjeh y Joiabqdt, Ifqdyq ew Iqkty-Qhqryq.
    1987 – Kjlyabuh ioijucuj veh å ijohu vøhuhbøiu jew veh Fqhyi HUH Q-bydzu.
    1986 – Yddwåh tud ijøhiju uaifehjaedjhqaj iec deudiyddu xqttu læhj lkdduj ql ud vhqdia lyhaiecxuj: Aecfbujj qkjecqjyiuhydw ql iudjhqbrqdaud y Iqkty Qhqryq.
    1981 – Lydduh aedjhqaj iec xelutudjhufhudøh y vehrydtubiu cut Jébéjub 3L-fheizuajuj, iec cqhauhju ijqhjud få bqdiuhydwud ql Cydyjub y Vhqdahyau.
    1978 – Ijuhyqi ydjuhdqizedqbu uaifqdized ijqhjuh cut ujqrbuhydwud ql tqjjuhiubiaqf y Iluyji.
    1973 – Yddwåh aedjhqaj ec qkjecqjyiuhydwifheizuaj veh Qwudsu Vhqdsu Fhuiiu.
    1969 – Ijuhyq whkddbuwwui ql Zuqd Sqhjuhed.
    1337 - IefhqIjuhyq{auufydw_kf_myjx_jxu_2I_xyijeho}

### Tips

Check out common encoding and enciphers!


## Basehunter 50

Drop the base.

    U29wcmFTdGVyaWF7QjY0OmIxbmFyeV90MF90M3h0XzNuYzBkMW5nfQ==

## Numbers everywhere 75

What does it mean?

    n: 25690482345878956844126846479665143813235654334579327772913434654639290215925805453462979298187476148765365326667509085275962716258157050378088331320408094938145781323480858939135609370247547099526519795849486399944191370811132469344392618461156310927699263667985116221128140608621172571013920384353306161391548756574773001499164964443056450461570880706774737931930132241303372958747997714357124880208372339130965982038663705838162421608420033733295588724745170454047044977131839342288901770954148796953330620820759615040414675245775408851539170385680144991204766047136753556198835041876134274600163315183807799425181

    d: 17126988230585971229417897653110095875490436223052885181942289769759526810617203635641986198791650765843576884445006056850641810838771366918725554213605396625430520882320572626090406246831698066351013197232990933296127580540754979562928412307437540618466175778656744147418760405747448380675946922902204107594152092636876219942618955042439288810900225245089347896568192241623700459052219948607139132225974505272654952269236306450167173499617329387825086006329600903981925678500256836100204486710319198778137648940628944036626437240032323844081165759516227190769561288822216094042796082385647222988346265167861593147243

    c: 26730382286000556531802018099980061325501391643410182181672395051947343089618338582609296012447824229606215370546154754900392310852418994179520435362645961617172214625283698704924528941339065725323312613942376976019325718815975231862025838364362292188107312303687247006525122134743955018086683284809096231051350665061

### Hints 
* Known crypto system.
* Checkout the Python library Crypto.Util and it's module "number". When you have figured out the mathematical equation, print the answer using `number.long_to_bytes(answer)`

## Ciphers at war 150
So, you know Sopra Steria by solving some other tasks. Did you know that Sopra Steria also won the Great Place To Work prize the last two years? Sopra Steria is a very nice place to work, and Sopra Steria focuses a lot on security and building teams having security knowledge when in projects.

Oh, I forgot.. You are here to solve a task. These ciphers are at war. Here, take this mixed alphabet! And, the key... It is hidden in plain sight.

    OR{Y_NBIPEFTHUASZC}LMXWGK
    
And at last, take this ciphertext:

    DXDFAGDXDFFDFGAAAAXAXDDAFDXAADFDAAXAFXDXXDAFDDFFFAFGGAFGGGGXFGAFFXDFAX

Good luck! Be careful in the war of ciphers.

### Hints
* This is the earlier version of the one used in the first war.
* Remember to always have camel case in flag: SopraSteria{...}, but all the other characters are lower case.