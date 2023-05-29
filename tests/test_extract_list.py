from click.testing import CliRunner
from gen_list.extract_list import output_list

# Needs to be relative to project root!
test_data_path = './tests/data/karl-das-krokodil.txt'

def test_has_expected_tokens():
    runner = CliRunner()
    result = runner.invoke(output_list, ['--input', test_data_path])
    assert result.exit_code == 0
    assert "beschloss" in result.output
    assert "Haus" in result.output
    assert "Anpassungsfähigkeit" in result.output

