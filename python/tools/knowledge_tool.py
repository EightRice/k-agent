import os
from agent import Agent
from . import online_knowledge_tool
from python.helpers import perplexity_search
from python.helpers import duckduckgo_search
from dotenv import dotenv_values
# Load the .env file
env_vars = dotenv_values(".env")

from . import memory_tool
import concurrent.futures



from python.helpers.tool import Tool, Response
from python.helpers import files

class Knowledge(Tool):
    def execute(self, question="", **kwargs):
        with concurrent.futures.ThreadPoolExecutor() as executor:
            # Schedule the two functions to be run in parallel

            # perplexity search, if API provided
            if env_vars.get("API_KEY_PERPLEXITY"):
                perplexity = executor.submit(perplexity_search.perplexity_search, question)
            else: perplexity = None

            # duckduckgo search
            duckduckgo = executor.submit(duckduckgo_search.search, question)

            # memory search
            future_memory = executor.submit(memory_tool.search, self.agent, question)

            # Wait for both functions to complete
            perplexity_result = (perplexity.result() if perplexity else "") or ""
            duckduckgo_result = duckduckgo.result()
            memory_result = future_memory.result()

        msg = files.read_file("prompts/tool.knowledge.response.md", 
                              online_sources = perplexity_result + "\n\n" + str(duckduckgo_result),
                              memory = memory_result )

        if self.agent.handle_intervention(msg): pass # wait for intervention and handle it, if paused

        return Response(message=msg, break_loop=False)