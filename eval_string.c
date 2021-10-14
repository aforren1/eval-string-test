#define PY_SSIZE_T_CLEAN
#include <Python.h>

int PsychRuntimeEvaluateString(const char* cmdstring)
{
#ifndef Py_LIMITED_API
    PyObject* res;
    res = PyRun_String(cmdstring, Py_file_input, PyEval_GetGlobals(), PyEval_GetLocals());
    if (res) {
        // Success! We don't have a use for the res'ults object yet, so just unref it:
        Py_DECREF(res);
        return(0);
    }
#else
    PyObject* code = Py_CompileString(cmdstring, "PTB", Py_file_input);
    if (code) {
        PyObject* res = PyEval_EvalCode(code, PyEval_GetGlobals(), PyEval_GetLocals());
        Py_DECREF(code);
        if (res) {
            Py_DECREF(res);
            return(0);
        }
    }
	printf("PTB-WARNING: Module tried to call PsychRuntimeEvaluateString(%s),\nwhich is *unsupported* in Py_LIMITED_API mode!!!\n", cmdstring);
#endif
    // Failed:
    return(-1);
}

PyDoc_STRVAR(eval_string__doc__, "fooo");
static PyObject *eval_string(PyObject *self, PyObject *args) {
    const char* cmd;
    if (!PyArg_ParseTuple(args, "s", &cmd)) {
        return NULL;
    }
    return PyLong_FromLong(PsychRuntimeEvaluateString(cmd));
}

static PyMethodDef eval_string_meths[] = {
    {"eval_string", eval_string, METH_VARARGS, eval_string__doc__},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef esm = {
    PyModuleDef_HEAD_INIT, "eval_string", NULL, -1, eval_string_meths
};

PyMODINIT_FUNC
PyInit_eval_string(void) {
    return PyModule_Create(&esm);
}
