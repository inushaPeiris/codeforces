#include <iostream>
#include <vector>
using namespace std;

int main() {
    vector<string> words;
    string word;
    int limit = 10;
    int inputCount;

    cin >> inputCount;

    while (inputCount) {
        cin >> word;
        words.push_back(word);
        inputCount--;
    }

    for (int i = 0; i < words.size(); i++) {
        string wrd = words[i];

        if (wrd.length() > limit) {
            int midNum = wrd.length() - 2;
            cout << wrd[0] << midNum << wrd[wrd.length() - 1] << endl;
        } else {
            cout << wrd << endl;
        }
    }
    
    return 0;
}
