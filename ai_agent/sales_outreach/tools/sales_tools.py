def create_sales_tools(sales_agent1, sales_agent2, sales_agent3):

    description = "Write a cold sales email"

    tool1 = sales_agent1.as_tool(
        tool_name="b2b_sales_email",
        tool_description=description
    )

    tool2 = sales_agent2.as_tool(
        tool_name="startup_sales_email",
        tool_description=description
    )

    tool3 = sales_agent3.as_tool(
        tool_name="enterprise_sales_email",
        tool_description=description
    )

    return [tool1, tool2, tool3]