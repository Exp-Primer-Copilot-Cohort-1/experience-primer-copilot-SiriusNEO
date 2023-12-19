#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main()
{
    vector<string> names;
    vector<int> scores;
    string name;
    int score;
    while (cin >> name >> score)
    {
        if (name == "NoName" && score == 0)
            break;
        names.push_back(name);
        scores.push_back(score);
    }
    for (int i = 0; i < names.size(); i++)
    {
        cout << names[i] << " " << scores[i] << endl;
    }
    return 0;
}
```