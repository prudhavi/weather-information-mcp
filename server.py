from mcp.server.fastmcp import FastMCP

from tools.weather_tool import weather_information



mcp = FastMCP(
    "Weather Information MCP"
)



@mcp.tool()
def get_weather(city:str):

    """
    Get current weather information
    """

    return weather_information(city)



if __name__ == "__main__":

    mcp.run()
