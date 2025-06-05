import asyncio
from agent import hello_world_agent

async def main():
    user_input = input("Ask anything: ")
    response = await hello_world_agent.run(user_input)
    print(response)

if __name__ == '__main__':
    asyncio.run(main())
