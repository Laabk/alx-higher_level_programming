#include <Python.h>
#include <stdio.h>

/**
 * print_python_list_info - this prints the python information 
 * list
 * @p: the Pythr=on Object
 * Return: nothing
 */
void print_python_list_info(PyObject *p)
{
	PyObject *theitem;
	long int arr, d;
	PyListObject *thelist;

	arr = Py_SIZE(p);
	printf("[*] Size of the Python List = %ld\n", arr);

	thelist = (PyListObject *)p;
	printf("[*] Allocated = %ld\n", thelist->allocated);

	for (d = 0; d < arr; d++)
	{
		theitem = PyList_GetItem(p, d);
		printf("Element %ld: %s\n", d, Py_TYPE(theitem)->tp_name);
	}
}
