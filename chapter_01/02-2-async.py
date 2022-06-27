import time
import asyncio


async def delivery(name, mealtime):
    print(f"{name}에게 배달 완료!")
    await asyncio.sleep(mealtime)
    print(f"{name} 식사 완료, {mealtime}시간 소요...")
    print(f"{name} 그릇 수거 완료")
    return mealtime


async def main():
    ## awaitable한 객체들이 gather안에 들어 있으면, 각각의 인자들이 동시성을 기반으로 실행 됨.
    result = await asyncio.gather(
        delivery("A", 1),
        delivery("B", 2),
        delivery("C", 3),
    )

    print(result)


if __name__ == "__main__":
    start = time.time()
    asyncio.run(main())
    end = time.time()
    print(end - start)
