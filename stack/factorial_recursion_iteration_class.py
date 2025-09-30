#############################################################################
#  시스템 스택 호출과 재귀함수를 이용한 팩토리얼 계산 콘솔 인터렉티브 프로그램 
#  작성자: 홍길동
#  작성일: 2024-09-15
# 순환(recursion)과 반복(iteration)의 차이점 이해
#  - 반복문 기반과 재귀 기반의 팩토리얼 계산 함수 구현
#  - 유효성 검사 포함 (0 이상 정수 확인)
#  - 문자열 입력 → 정수 변환 → 유효성 검사 → 팩토리얼 계산까지 포함된 콘솔 프로그램 형태
#  - q 또는 quit 입력 시 종료
#############################################################################
import sys
import time

def factorial_iter(n):
    # 반복문 기반 n! 계산
    result = 1
    if n == 0:
        return result
    else:
        for k in range(2, n + 1):
            result *= k
    return result

def factorial_rec(n):
    # 재귀 기반 n! 계산
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_rec(n - 1)

def run_with_time(func, n: int):
    # 지정된 팩토리얼 함수(func) 실행 시간 측정 및 결과 반환
    start = time.perf_counter()
    result = func(n)
    end = time.perf_counter()
    elapsed = end - start
    return result, elapsed

if __name__ == "__main__":
    TEST_DATA = [0, 1, 2, 3, 5, 10, 15, 20, 30, 50, 100]

    while True:
        print("\n================ Factorial Tester ================")
        print("1) 반복법으로 n! 계산")
        print("2) 재귀로 n! 계산")
        print("3) 두 방식 모두 계산 후 결과/시간 비교")
        print("4) 준비된 테스트 데이터 일괄 실행")
        print("q) 종료")
        print("--------------------------------------------------")
        text = input("선택 : ").strip()

        if text.lower() in ['q', 'quit']:
            print("종료합니다.")
            sys.exit()

        elif text == '1':
            value = input("n 값(정수, 0 이상)을 입력하세요: ")
            try:
                num = int(value)
                result, t = run_with_time(factorial_iter, num)
                print(f"[반복] {num}! = {result}")
                print(f"실행 시간: {t:.6f}초")
            except ValueError:
                print("정수(0 이상의 숫자)만 입력하세요.")

        elif text == '2':
            value = input("n 값(정수, 0 이상)을 입력하세요: ")
            try:
                num = int(value)
                result, t = run_with_time(factorial_rec, num)
                print(f"[재귀] {num}! = {result}")
                print(f"실행 시간: {t:.6f}초")
            except ValueError:
                print("정수(0 이상의 숫자)만 입력하세요.")

        elif text == '3':
            value = input("n 값(정수, 0 이상)을 입력하세요: ")
            try:
                num = int(value)
                iter_result, iter_time = run_with_time(factorial_iter, num)
                rec_result, rec_time = run_with_time(factorial_rec, num)

                print(f"[반복] {num}! = {iter_result}")
                print(f"[재귀] {num}! = {rec_result}")
                print(f"일치 여부: {'일치' if iter_result == rec_result else '불일치'}")
                print(f"[반복] 시간: {iter_time:.6f}s | [재귀] 시간: {rec_time:.6f}s")

            except ValueError:
                print("정수(0 이상의 숫자)만 입력하세요.")

        elif text == '4':
            print("테스트 데이터 실행")
            for n in TEST_DATA:
                print(f"\nn = {n}")
                try:
                    iter_result, iter_time = run_with_time(factorial_iter, n)
                    rec_result, rec_time = run_with_time(factorial_rec, n)

                    print(f"[반복] 결과: {iter_result}")
                    print(f"[재귀] 결과: {rec_result}")
                    print(f"일치 여부: {'일치' if iter_result == rec_result else '불일치'}")
                    print(f"[반복] 시간: {iter_time:.6f}s | [재귀] 시간: {rec_time:.6f}s")

                except RecursionError:
                    print("[재귀] RecursionError 발생 - 너무 깊은 재귀입니다.")
                except ValueError as e:
                    print("[오류]", e)

        else:
            print("잘못된 메뉴 선택입니다. 다시 선택해주세요.")