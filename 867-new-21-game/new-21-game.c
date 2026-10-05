double new21Game(int n, int k, int maxPts) {
    if (k == 0 || n >= k + maxPts - 1) return 1.0;
    if (n < k) return 0.0;
    double dp[k + maxPts];
    memset(dp, 0, sizeof(dp));
    dp[0] = 1.0;
    double window = 1.0;
    double ans = 0.0;
    for (int i = 1; i <= n; i++) {
        dp[i] = window / maxPts;
        if (i < k) {
            window += dp[i];
        } else {
            ans += dp[i];
        }
        if (i - maxPts >= 0) {
            window -= dp[i - maxPts];
        }
    }
    return ans;
}