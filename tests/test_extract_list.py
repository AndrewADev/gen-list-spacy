from click.testing import CliRunner
from gen_list.extract_list import generate_list

# Needs to be relative to project root!
test_data_path = './tests/data/karl-das-krokodil.txt'

def test_has_expected_tokens():
    runner = CliRunner()
    result = runner.invoke(generate_list, ['--input', test_data_path])
    assert result.exit_code == 0
    assert "beschloss" in result.output
    assert "Haus" in result.output
    assert "Anpassungsfähigkeit" in result.output

def test_exports_to_csv():
    runner = CliRunner()
    result = runner.invoke(generate_list, args=['--input', test_data_path, '--output-type', 'csv'])
    assert result.exit_code == 0
    assert "Token" in result.output # header
    assert "Haus" in result.output
    assert "Anpassungsfähigkeit" in result.output
