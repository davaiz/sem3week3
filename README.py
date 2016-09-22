# sem3week3

#include <iostream>

using namespace std;

void bad_incrementor(int x)
{
    x++;
    std::cout << "x changed: " << x << std::endl;
}

int main()
{
    int c = 1;
    bad_incrementor(c);
    std::cout << c;
    return 0;
}





#include <iostream>

using namespace std;

void good_incrementor(int *x)
{
    (*x)++;
}

int main()
{
    int x = 1;
    std::cout << "x initial: " << x << std::endl;
    good_incrementor(&x);
    std::cout << "x changed: " << x << std::endl;

    return 0;
}





#include <iostream>

using namespace std;

void better_incrementor(int &x)
{
    x++;
}

int main()
{
    int x = 1;
    std::cout << "x initial: " << x << std::endl;
    better_incrementor(x);
    std::cout << "x changed: " << x << std::endl;

    return 0;
}
