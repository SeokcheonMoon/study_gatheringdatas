import courtauction_ui_Select_selector_subfunction as subfunction   #Import A as B : A라는 파일을 B라고 칭하겠다는 의미


def main() :
    try:
        uri="https://www.courtauction.go.kr/"
        browser = subfunction.getBrowserFromURI(uri)    # 업무 코드
        browser = subfunction.clickThingsCourt(browser)
        court_count = subfunction.selectCourts(browser=browser)
        print("court count : {}".format(court_count))
    except:
        pass    # 업무 코드 문제 발생 시 대처 코드
    finally :
        subfunction.quitBrowser(browser=browser)    # try나 except이 끝난 후 무조건 실행 코드
    return 0

if __name__ == "__main__":
    try:
        main()    # 업무 코드
    except:
        pass    # 업무 코드 문제 발생 시 대처 코드
    finally :
        pass    # try나 except이 끝난 후 무조건 실행 코드