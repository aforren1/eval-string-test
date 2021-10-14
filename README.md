LIMITED=1 pip wheel . -w dist/ --build-option --py-limited-api=cp37

pip wheel . -w dist/

pip install dist/eval_string-0.0.1-cp37-abi3-linux_x86_64.whl --force-reinstall

pip install dist/eval_string-0.0.1-cp39-cp39-linux_x86_64.whl --force-reinstall
