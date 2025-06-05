from __future__ import annotations
from pydantic_ai import Agent, RunContext

class HelloWorldAgent(Agent):
    async def run(self, user_input: str) -> str:
        """Responds with 'Hello, World!' to any input given.

        Args:
            user_input: The input from the user.

        Returns:
            A string response saying 'Hello, World!'.
        """
        return "Hello, World!"

hello_world_agent = HelloWorldAgent()
