#include <Python.h>
#include <stdio.h>

/**
 * Print information about a Python list.
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t list_size = PyList_Size(p);
	Py_ssize_t allocated_size = ((PyListObject *)p)->allocated;
	PyObject *element;

	printf("[*] Size of the Python List = %ld\n", list_size);
	printf("[*] Allocated = %ld\n", allocated_size);
	
	for (Py_ssize_t i = 0; i < list_size; i++)
	{
		element = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(element)->tp_name);
	}
}
