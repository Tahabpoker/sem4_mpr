#include <stdio.h>
#include <stdbool.h>

#define MAX 100

bool dp[MAX][MAX];

void printSubset(int set[], int n, int sum, int subset[], int subsetSize) {
    if (sum == 0) {
        for (int i = 0; i < subsetSize; i++)
            printf("%d ", subset[i]);
        printf("\n");
        return;
    }
    if (n == 0 || sum < 0)
        return;
    if (dp[n - 1][sum]) 
        printSubset(set, n - 1, sum, subset, subsetSize);
    if (sum >= set[n - 1] && dp[n - 1][sum - set[n - 1]]) {
        subset[subsetSize] = set[n - 1];
        printSubset(set, n - 1, sum - set[n - 1], subset, subsetSize + 1);
    }
}

void subsetSum(int set[], int n, int sum) {
    for (int i = 0; i <= n; i++)
        dp[i][0] = true;
    for (int i = 1; i <= sum; i++)
        dp[0][i] = false;
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= sum; j++) {
            if (j < set[i - 1])
                dp[i][j] = dp[i - 1][j];
            else
                dp[i][j] = dp[i - 1][j] || dp[i - 1][j - set[i - 1]];
        }
    }
    if (dp[n][sum]) {
        int subset[n];
        printSubset(set, n, sum, subset, 0);
    }
}

int main() {
    int set[] = {10, 7, 5, 18, 12, 20, 15};
    int sum = 35;
    int n = sizeof(set) / sizeof(set[0]);
    subsetSum(set, n, sum);
    return 0;
}
