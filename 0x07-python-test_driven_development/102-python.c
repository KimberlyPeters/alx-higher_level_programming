#include <stdio.h>
#include <Python.h>

/**
 * print_python_string - Prints string information
 *
 * @p: Python Object
 * Return: No return value
 */
void print_python_string(PyObject *p)
{
	PyObject *str_obj, *repr_obj;

	(void)repr_obj;
	printf("[.] string object info\n");

	if (strcmp(p->ob_type->tp_name, "str") != 0)
	{
		printf("  [ERROR] Invalid String Object\n");
		return;
	}

	if (PyUnicode_IS_COMPACT_ASCII(p))
		printf("  type: compact ascii\n");
	else
		printf("  type: compact unicode object\n");

	repr_obj = PyObject_Repr(p);
	str_obj = PyUnicode_AsEncodedString(p, "utf-8", "~E~");
	printf("  length: %ld\n", PyUnicode_GET_LENGTH(p));
	printf("  value: %s\n", PyBytes_AS_STRING(str_obj));
}
