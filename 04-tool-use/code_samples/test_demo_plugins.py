from demo_tool_agent import TimePlugin, CalculatorPlugin

def test_calculator_add():
    calc = CalculatorPlugin()
    result = calc.add(5, 7)
    assert result == 12
    print("test_calculator_add passed")

def test_calculator_subtract():
    calc = CalculatorPlugin()
    result = calc.subtract(10, 4)
    assert result == 6
    print("test_calculator_subtract passed")

def test_time_plugin():
    # We can't easily test exact time, but we can check format
    time_plugin = TimePlugin()
    time_str = time_plugin.get_current_time()
    # Expect format YYYY-MM-DD HH:MM:SS
    assert len(time_str) == 19
    assert "-" in time_str
    assert ":" in time_str
    print("test_time_plugin passed")

if __name__ == "__main__":
    try:
        test_calculator_add()
        test_calculator_subtract()
        test_time_plugin()
        print("All tests passed!")
    except AssertionError as e:
        print(f"Test failed: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
