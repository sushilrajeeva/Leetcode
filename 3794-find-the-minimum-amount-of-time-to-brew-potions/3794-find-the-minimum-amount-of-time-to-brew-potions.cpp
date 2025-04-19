#include <vector>
#include <algorithm>

class Solution {
public:
    long long minTime(std::vector<int>& skill, std::vector<int>& mana) {
        int n = static_cast<int>(skill.size());
        int m = static_cast<int>(mana.size());

        std::vector<long long> prev(n, 0);                 // prev column (T[·][j‑1])

        for (int j = 0; j < m; ++j) {
            std::vector<long long> temp(n, 0);             // current column (T[·][j])

            // ---------- left‑to‑right sweep ----------
            for (int i = 0; i < n; ++i) {
                long long left = (i == 0) ? 0               : temp[i - 1];
                long long up   = prev[i];
                temp[i] = 1LL * skill[i] * mana[j] + std::max(left, up);
            }

            // ---------- right‑to‑left “reverse” sweep ----------
            long long last = 1LL * skill[n - 1] * mana[j];
            for (int k = n - 2; k >= 0; --k) {
                temp[k] = std::max(temp[k], temp[k + 1] - last);
                last    = 1LL * skill[k] * mana[j];
            }

            prev.swap(temp);                               // roll column
        }

        return prev.back();                                // T[n‑1][m‑1]
    }
};
