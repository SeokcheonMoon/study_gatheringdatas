# * 웹 크롤링 동작
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

webdriver_manager_directory = ChromeDriverManager().install()
browser = webdriver.Chrome(service=ChromeService(webdriver_manager_directory))
# ChromeDriver 실행

# Chrome WebDriver의 capabilities 속성 사용
capabilities = browser.capabilities

# - 주소 입력
browser.get("https://www.coupang.com/np/categories/413812")

# - 가능 여부에 대한 OK 받음
pass
# - html 파일 받음(and 확인)
html = browser.page_source
print(html)

# - 정보 획득 ---------------------------------------------------정보 획득 시 거의 고정되는 문구
from selenium.webdriver.common.by import By


selector_value = "div.name"
elements_path = browser.find_elements(by = By.CSS_SELECTOR, value = selector_value) 
              
for webelement in elements_path :                
    title = webelement.text
    print("{}".format(title))
    pass

pass

# 아이든 2단폴더 요가 홈트 매트, 아이보리
# 프로스펙스 라텍스밴드, 퍼플
# 마이솔 EVA 요가 필라테스 마사지 스트레칭 폼롤러, 그린 민트
# 슈퍼비스트 무릎보호대[일반] 양쪽2개 1세트 시즌온헬스아대 SUPERBEAST KNEE, SS(47cm이하), 2개
# 마이웨잇 파워 홈트 밴드 3종 + 파우치 세트, 화이트, 그레이, 블랙
# 스마트공간 운동 매트, 퍼플
# 에코리즈_ 네오롤러 하드타입, 블랙
# 앳플리 코어 필라테스 요가 운동 루프밴드 5종 세트, 멜로우 아이보리, 디티 핑크, 고스애머 그린, 베릴 그린, 코코아 브라운
# 아리프 애플힙 스쿼트 밴드 3종 세트, LV01 민트, LV02 퍼플, LV03 핑크, 1세트
# 코멧 EVA 편안한 폼롤러, 와인 (91cm)
# 아리프 가든 스텝박스 2단, 혼합색상
# 이고진 NBR 프리미엄 요가매트, 라벤더
# 잠스트 발목보호대 A1-S, 1개
# 마더케이솔루티오 밸런스 손목 보호대 블랙 3p, 1세트
# 아리프 NBR 쿠션 요가매트 13mm, 러블리핑크, 1개
# 셀프리쉬 울트라 패스트업 EMS 마사지기, 혼합색상
# 밸런시스 TPE 요가 매트 + 가방, 화이트퍼플
# 에바핏 범프스 마사지 폼 롤러, 블루그린
# 비핏 요가매트 TPE 10mm, 네추럴 크림
# [인포벨 홈쇼핑]엑스킹 에어 스텝퍼 파워 홈트 뱃살 하체 유산소 운동기구 스테퍼 스태퍼 스탭퍼, 스카이블루
# 코멧 스포츠 싱글 마사지볼 + 땅콩 마사지볼 세트, 퍼플, 1세트
# 이고진 NBR 프리미엄 요가매트, 샌드
# 아이돈케어 스포츠 EVA 마사지 스트레칭 폼롤러, 라이트 블루
# 코어바디 반원형 폼 롤러, 블루마블
# 트라택 3D 범프 폼롤러 + 운동법 포스터 세트, 다크네이비(폼롤러), 1세트
# 아이워너 2인용 트램폴린, 핑크
# 호스커스 EVA 폼롤러, 인디핑크
# SHIELD 손목 보호대 리스트랩 모던블랙 2p, 1개
# 트라택 TPE 리버서블 요가매트, 올리브그레이 + 브라운 (눈금있음)
# 피어니스트 가정용 스텝퍼, 블랙 + 화이트
# 아이워너 네오프렌 삼각아령 1kg x 2p + 1.5kg x 2p + 3kg x 2p + 아령거치대 세트, 1세트
# 인트로미 라르고 폼롤러, 스톤그레이
# 코멧 홈트용 요가매트 2단, 그레이
# 이고진 8320 스텝퍼, 블랙핑크
# 트라택 EPP 폼롤러 원형, 샌드베이지
# 트로비스 스트레칭 바, 혼합색상
# 아리프 네오프렌 선인장 아령, 4kg, 2개
# 큐잉 필라테스 요가 EVA 폼롤러, 코랄 + 블루, 1개
# 세라밴드 2M 오리지널 밴드 단계별 탄성저항 밴드 +운동매뉴얼, 실버(6단계), 1개
# 세라밴드 CLX 밴드 단계별 탄성저항 루프형 밴드 +운동매뉴얼, 그린(3단계)
# 이고진 요가매트 NBR 프리미엄, 라이트 핑크
# 밸런시스 필라테스 링, 바이올렛
# 가네샤요가프랍스 더 가네샤 요가매트 라이트 3MM, Midnight Blue
# 가네샤요가프랍스 더 가네샤 요가매트 울트라컴포트 [ 6mm ], Storm Blue
# 트로비스 스트롱 파워밴드 7단계, 스카이, 1개
# 아리프 다이나믹 옥타곤 아령, 15kg, 1개입
# 아리프 네오프렌 삼각 아령 1kg 2p + 2kg 2p + 3kg 2p + 거치대 세트, 1세트
# 아리프 네오프렌 선인장 아령, 5kg, 2개
# 에이더 마우스 고리형 게임 그림 프로타입1 손목보호대 오른쪽 217660, 1개
# 와두 밸런스 NBR 요가매트 15mm, 코스믹라떼, 그레이(스트랩)
# 프로스펙스 라텍스밴드, 딥블루
# 로베라 사이드 스텝퍼 M-90T, 화이트
# 아리프 지압 훌라후프 1.6kg, 핑크 + 그레이
# 에르고바디 핏유어코어 허리보호대 L, 1개
# 엑사이더 접이식 실내자전거, CF1000C, 화이트

