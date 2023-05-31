#include <stdio.h>
#include <Python.h>

/**
 * print_python_bytes - print some basic info about Python lists,
 * Python bytes an Python float objects.
 *
 * @p: Pointer to Python Object
 * Return: no return
 */

void print_python_bytes(PyObject *p)
{
	char *str;
	long int size, n, limit;

	setbuf(stdout, NULL);

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		setbuf(stdout, NULL);
		return;
	}

	size = ((PyVarObject *)(p))->ob_size;
	str = ((PyBytesObject *)p)->ob_sval;

	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", str);

	if (size >= 10)
		limit = 10;
	else
		limit = size + 1;

	printf("  first %ld bytes:", limit);

	for (n = 0; n < limit; n++)
		if (str[n] >= 0)
			printf(" %02x", str[n]);
		else
			printf(" %02x", 256 + str[n]);

	printf("\n");
	setbuf(stdout, NULL);
}

/**
 * print_python_float - Prints the float information
 *
 * @p: Pointer to Python Object
 * Return: no return
 */

void print_python_float(PyObject *p)
{
	double value;
	char *ptr;

	setbuf(stdout, NULL);
	printf("[.] float object info\n");

	if (!PyFloat_Check(p))
	{
		printf("  [ERROR] Invalid Float Object\n");
		setbuf(stdout, NULL);
		return;
	}

	value = ((PyFloatObject *)(p))->ob_fvalue;
	ptr = PyOS_double_to_string(value, 'r', 0, Py_DTSF_ADD_DOT_0, Py_DTST_FINITE);

	printf("  value: %s\n", ptr);
	setbuf(stdout, NULL);
}

/**
 * print_python_list - Prints the list information
 *
 * @p: Pointer to the Python Object
 * Return: no return
 */

void print_python_list(PyObject *p)
{
	long int size, i;
	PyListObject *list;
	PyObject *my_obj;

	setbuf(stdout, NULL);
	printf("[*] Python list info\n");

	if (!PyList_Check(p))
	{
		printf("  [ERROR] Invalid List Object\n");
		setbuf(stdout, NULL);
		return;
	}

	size = ((PyVarObject *)(p))->ob_size;
	list = (PyListObject *)p;

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", list->allocated);

	for (i = 0; i < size; i++)
	{
		my_obj = list->ob_item[i];
		printf("Element %ld: %s\n", i, ((my_obj)->ob_type)->tp_name);

		if (PyBytes_Check(my_obj))
			print_python_bytes(my_obj);
		if (PyFloat_Check(my_obj))
			print_python_float(my_obj);
	}
	setbuf(stdout, NULL);
}
