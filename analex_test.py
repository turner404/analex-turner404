import pytest
import subprocess
import shlex
import os
import fnmatch

import analex

test_cases = [("", "-k"), ("teste.c", "-k"), ("notexists.cm", "-k")]

for file in fnmatch.filter(os.listdir('tests'), '*.cm'):
    test_cases.append((file, "-k"))

@pytest.mark.parametrize("input_file, args", test_cases)
def test_execute(input_file, args):
    if input_file != '':
        path_file = 'tests/' + input_file
    else:
        path_file = ""

    cmd = f"python analex.py {args} {path_file}"
    process = subprocess.Popen(shlex.split(cmd), stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    stdout, stderr = process.communicate()  # Captura a saída do processo

    path_file = f'tests/{input_file}'
    output_file_path = path_file + ".lex.out"

    if not os.path.exists(output_file_path):
        pytest.fail(f"Arquivo esperado de saída '{output_file_path}' não encontrado.")

    with open(output_file_path, "r", encoding="utf-8") as output_file:
        expected_output = output_file.read()

    print("Generated output:")
    print(stdout.decode("utf-8"))

    print("Expected output:")
    print(expected_output)

    assert stdout.decode("utf-8").replace("\r\n", "\n").strip() == expected_output.replace("\r\n", "\n").strip()
