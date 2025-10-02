#############################################################################
#  시스템 스택 호출과 재귀함수를 이용한 팩토리얼 계산 콘솔 인터렉티브 프로그램
#  작성자: 주성준
#  작성일: 2025-09-29
# 순환(recursion)과 반복(iteration)의 차이점 이해
#  - 반복문 기반과 재귀 기반의 팩토리얼 계산 함수 구현
#  - 유효성 검사 포함 (0 이상 정수 확인)
#  - 문자열 입력 → 정수 변환 → 유효성 검사 → 팩토리얼 계산까지 포함된 콘솔 프로그램 형태
#  - q 또는 quit 입력 시 종료
#############################################################################
import sys
import time

def factorial_iter(n):
    if n < 0:
        raise ValueError("음수는 팩토리얼을 계산할 수 없습니다.")
    value = 1
    for k in range(2, n + 1):
        value *= k
    return value

def factorial_rec(n):
    if n < 0:
        raise ValueError("음수는 팩토리얼을 계산할 수 없습니다.")
    if n == 0 or n == 1:
        return 1
    return n * factorial_rec(n - 1)

def run_with_time(func, n: int):
    # 지정된 팩토리얼 함수 실행 시간 측정 및 결과 반환
    start = time.perf_counter()
    result = func(n)
    end = time.perf_counter()
    elapsed = end - start
    return result, elapsed

def get_valid_number():
    # 0 이상의 정수를 입력받는 함수
    value = input("n 값(정수, 0 이상)을 입력하세요: ").strip()

    if not value.isdigit():
        print("정수(0 이상의 숫자)만 입력하세요.")
        return None

    num = int(value)
    if num < 0:
        print("정수(0 이상의 숫자)만 입력하세요.")
        return None
    return num

if __name__ == "__main__":
    TEST_DATA = [0, 1, 2, 3, 5, 10, 15, 20, 30, 50, 100]

    print("팩토리얼 계산기 (반복/재귀) - 정수 n>=0 를 입력하세요.\n")

    while True:
        print("================ Factorial Tester ================")
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
            num = get_valid_number()
            if num is None:
                continue

            try:
                result, t = run_with_time(factorial_iter, num)
                print(f"[반복] {num}! = {result}")
                print(f"실행 시간: {t:.6f}초")

            except ValueError as e:
                print(e)
            except RecursionError:
                print("재귀 호출 깊이가 너무 깊습니다.")

        elif text == '2':
            num = get_valid_number()
            if num is None:
                continue
            try:
                result, t = run_with_time(factorial_rec, num)
                print(f"[재귀] {num}! = {result}")
                print(f"실행 시간: {t:.6f}초")

            except ValueError as e:
                print(e)
            except RecursionError:
                print("재귀 호출 깊이가 너무 깊습니다.")

        elif text == '3':
            num = get_valid_number()
            if num is None:
                continue
            try:
                iter_result, iter_time = run_with_time(factorial_iter, num)
                rec_result, rec_time = run_with_time(factorial_rec, num)

                print(f"[반복] {num}! = {iter_result}")
                print(f"[재귀] {num}! = {rec_result}")
                print(f"일치 여부: {'일치' if iter_result == rec_result else '불일치'}")
                print(f"[반복] 시간: {iter_time:.6f}s | [재귀] 시간: {rec_time:.6f}s")

            except ValueError as e:
                print(e)
            except RecursionError:
                print("재귀 호출 깊이가 너무 깊습니다.")

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

                except ValueError as e:
                    print(e)
                except RecursionError:
                    print("재귀 호출 깊이가 너무 깊습니다.")

        else:
            print("잘못된 메뉴입니다.")
