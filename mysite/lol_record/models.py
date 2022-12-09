from django.db import models

# Create your models here.
class champion(models.Model):
    id = models.AutoField(primary_key=True) #ㄱ~ㅎ 순으로 정렬된 챔피언들을 순서대로 id 부여
    name = models.CharField(max_length=50) #챔피언 영문 이름 (가렌 -> garen)
    imgurl = models.URLField(max_length=500) #챔피언 프로필 이미지 url (출처 : 나무위키)
    #img = models.ImageField()

class todaystotal(models.Model): #전적 페이지에 있음 // 당일 총 경기 요약
    victory = models.IntegerField() #승리 횟수
    defeat = models.IntegerField() #패배 횟수
    draw = models.IntegerField() #다시하기 횟수
    total = models.IntegerField() #전체 게임 횟수

class game(models.Model): #경기정보
    gameid = models.AutoField(primary_key=True) #500경기 이후론 삭제
    rnk = models.TextField() #=ranking // 래더랭킹(?위, 상위 n%)
    kog = models.TextField() #=kind of game // 게임종류(솔랭, 자랭, 일반, 칼바람, TFT, ..)
    vod = models.TextField() #=victory or defeat //승패 여부
    gmt = models.TextField() #=game time // 게임 진행 시간
    champion_id = models.ForeignKey('champion',on_delete=models.CASCADE,blank=True) # champion_id
    kda = models.TextField() #=kill death assist // 킬뎃어시
    gpa = models.TextField() #=grade poing arrange // 평점 형식 => [(킬 수 + 어시스트 수)/데스 수] ': 1 평점'
    prk = models.TextField() #=participation rate of kill // 킬관여율 형식 => [((k+1)/우리팀 전체 킬 수)*100] {소숫점 첫째자리 반올림 ex) 49.2324 => 49%}
    ccw = models.TextField() #=count of control wad // 제어와드 갯수
    ccs = models.TextField() #=count of cs // cs 갯수
    prt = models.TextField() #=present tier // 현재 티어

class life_achievement(models.Model): #인생업적
    achievementid = models.AutoField(primary_key=True) #저장목록 id
    rnk = models.TextField() #=ranking // 래더랭킹(?위, 상위 n%)
    kog = models.TextField() #=kind of game // 게임종류(솔랭, 자랭, 일반, 칼바람, TFT, ..)
    vod = models.TextField() #=victory or defeat //승패 여부
    gmt = models.TextField() #=game time // 게임 진행 시간
    game_id = models.ForeignKey('game',on_delete=models.CASCADE,) # champion_id
    kda = models.TextField() #=kill death assist // 킬뎃어시
    gpa = models.TextField() #=grade poing arrange // 평점 형식 => [(킬 수 + 어시스트 수)/데스 수] ': 1 평점'
    prk = models.TextField() #=participation rate of kill // 킬관여율 형식 => [((k+1)/우리팀 전체 킬 수)*100] {소숫점 첫째자리 반올림 ex) 49.2324 => 49%}
    ccw = models.TextField() #=count of control wad // 제어와드 갯수
    ccs = models.TextField() #=count of cs // cs 갯수
    prt = models.TextField() #=present tier // 현재 티어
