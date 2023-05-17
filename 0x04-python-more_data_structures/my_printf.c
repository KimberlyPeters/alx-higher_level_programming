#include <stdarg.h>
#include <unistd.h>
#include <stdio.h>

static void my_putchar(char c)
{
	write(1, &c, 1);
}

static void my_putstr(const char *str)
{
	while (*str != '\0')
	{
		my_putchar(*str);
		str++;
	}
}

static void my_putint(int n)
{
	if (n < 0)
	{
		my_putchar('-');
		n = -n;
	}
	if (n >= 10)
	{
		my_putint(n / 10);
	}
	my_putchar('0' + (n % 10));
}

int my_printf(const char* format, ...)
{
	va_list args;
	va_start(args, format);
	
	int count = 0;
	const char* ptr = format;
	while (*ptr != '\0')
	{
		if (*ptr == '%')
		{
			// Handle format specifier
			ptr++; // Move past '%'
			if (*ptr == 'd' || *ptr == 'i')
			{
				int num = va_arg(args, int);
           			// Handle printing integer
				my_putint(num);
				count++;
			}
			else if (*ptr == 'u')
			{
				unsigned int num = va_arg(args, unsigned int);
              			// Handle printing unsigned integer
				my_putint(num);
				count++;
			}
			else if (*ptr == 'o')
			{
				unsigned int num = va_arg(args, unsigned int);
                		// Handle printing octal number
				unsigned int temp = num;
				int length = 0;
				while (temp != 0)
				{
					temp /= 8;
					length++;
				}
				if (num == 0)
					length = 1;
				temp = num;
				while (length > 0)
				{
					my_putchar('0' + (temp >> (3 * (length - 1)) & 7));
					length--;
					count++;
				}
			}
			else if (*ptr == 'x')
			{
				unsigned int num = va_arg(args, unsigned int);
             			// Handle printing hexadecimal number
				unsigned int temp = num;
				int length = 0;
				while (temp != 0)
				{
					temp /= 16;
					length++;
				}
				if (num == 0)
					length = 1;
				temp = num;
				while (length > 0)
				{
					int digit = temp >> (4 * (length - 1)) & 15;
					if (digit < 10)
						my_putchar('0' + digit);
					else
						my_putchar('a' + digit - 10);
					length--;
					count++;
				}
			}
			else if (*ptr == 'c')
			{
				char ch = (char)va_arg(args, int);
                		// Handle printing character
				my_putchar(ch);
				count++;
			}
			else if (*ptr == 's')
			{
				char* str = va_arg(args, char*);
                		// Handle printing string
				if (str == NULL)
					str = "(null)"; // Handle null string
				while (*str != '\0')
				{
					my_putchar(*str);
					str++;
					count++;
				}
			}
			else if (*ptr == 'p')
			{
				void* ptr = va_arg(args, void*);
				unsigned long address = (unsigned long)ptr;
				unsigned long temp = address;
				int length = 0;
				while (temp != 0)
				{
					temp /= 16;
					length++;
				}
				if (address == 0)
					length = 1;
				my_putstr("0x");
				while (length > 0)
				{
					int digit = address >> (4 * (length - 1)) & 15;
					if (digit < 10)
						my_putchar('0' + digit);
					else
						my_putchar('a' + digit - 10);
					length--;
					count++;
				}
			}
			
			va_end(args);
			return count;
		}
	}
}
