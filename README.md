# 

you need to install youtube-dl and some python libs like bs4

instructions:
1. download ymq.me url to local file, like http://apply.ymq.me/Index/Index/match_all/id/944.html to 2018.9.8中科大60周年校庆五羽轮比团体赛.htm
2. python3 ymqMp4Dl.py 2018.9.8中科大60周年校庆五羽轮比团体赛.htm
3. sh dl_ymq.sh

#usage: python3 ymqMp4Dl.py [-h] [-v] [-o OUTPUT] fileName
#
#manual to this script
#
#optional arguments:
#  -h, --help            show this help message and exit
#  -v, --verbosity       increase output verbosity
#  -o OUTPUT, --output OUTPUT
#                        output file name

### operation logs for instance ###
lguibin@ubuntu:~/Python/ymq.me-match-video-download$ py ymqMp4Dl.py ../temp/2018古劳镇“商会杯”羽毛球邀请赛.html -o ../temp/2018古劳镇“商会杯”羽毛球邀请赛.sh
## Info : save result to :  ../temp/2018古劳镇“商会杯”羽毛球邀请赛.sh
###--- 2018古劳镇“商会杯”羽毛球邀请赛 72 matches ---###
youtube-dl -o 男双1_半决赛_[默认分组021]_2018-08-25_16:30_场地2_20A1_2:0_B2_谭新_邹敏明_21:17_21:12_马双云_黄冠杰.mp4 http://pili-media.live.ymq.me/recordings/z1.ymq-live.5b7f9ede20a05d2e78016281/1535186973.m3u8
youtube-dl -o 男双1_半决赛_[默认分组022]_2018-08-25_16:30_场地4_20A2_2:0_B1_王文乐_温嘉祺_21:16_21:19_林贻健_张家洪.mp4 http://pili-media.live.ymq.me/recordings/z1.ymq-live.5b7f9f2da95be7503201468a/1535187035.m3u8
youtube-dl -o 男双2_半决赛_[默认分组021]_2018-08-25_16:50_场地2_20A1_2:0_B2_杜海燕_黄伟生_21:10_21:11_谭伟标_吕振梁.mp4 http://pili-media.live.ymq.me/recordings/z1.ymq-live.5b7f9ede20a05d2e78016281/1535186853.m3u8
youtube-dl -o 男双2_半决赛_[默认分组022]_2018-08-25_16:50_场地4_20A2_2:0_B1_冯俊浩_温嘉宁_21:14_21:16_张振辉_杨乃树.mp4 http://pili-media.live.ymq.me/recordings/z1.ymq-live.5b7f9f2da95be7503201468a/1535187065.m3u8
youtube-dl -o 男双1_三四名决赛_[默认分组024]_第19场_场地4_022_1F_0:3_2_2F_吕振梁_马双云_15:21_15:21_林贻健_张家洪.mp4 http://pili-media.live.ymq.me/recordings/z1.ymq-live.5b7f9f2da95be7503201468a/1535188912.m3u8
youtube-dl -o 男双2_决赛_[默认分组023]_第20场_场地2_122_1S_1:2_2_2S_杜海燕_黄伟生_15:21_21:19_10:21_温嘉宁_温嘉祺.mp4 http://pili-media.live.ymq.me/recordings/z1.ymq-live.5b7f9ede20a05d2e78016281/1535193091.m3u8
youtube-dl -o 男双2_三四名决赛_[默认分组024]_第20场_场地4_122_1F_0:3_2_2F_谭伟标_黄冠杰_21:16_16:21_10:21_罗全_梁志文.mp4 http://pili-media.live.ymq.me/recordings/z1.ymq-live.5b7f9f2da95be7503201468a/1535190155.m3u8
youtube-dl -o 混双_决赛_[默认分组023]_第21场_场地2_022_1S_1:2_2_2S_梁嘉文_任屏屏_4:21_2:21_王文乐_冯智昭.mp4 http://pili-media.live.ymq.me/recordings/z1.ymq-live.5b7f9ede20a05d2e78016281/1535193811.m3u8
###---Total 8 match Videos ---###
save result to excutable file : ../temp/2018古劳镇“商会杯”羽毛球邀请赛.sh


### todo list ###
1. input web url instead of save to local html file


