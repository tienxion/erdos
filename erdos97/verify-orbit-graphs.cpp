// Exhaustive finite graph check for a restricted Erdős #97 construction.
// This checks combinatorial consequences of separately proved geometric
// lemmas. It does not certify coordinates or solve #97.
#include <array>
#include <cstdint>
#include <iostream>
#include <utility>
#include <vector>

int main() {
  for (int n : {5, 6}) {
    std::vector<std::pair<int, int>> pairs;
    for (int i = 0; i < n; ++i)
      for (int j = i + 1; j < n; ++j) pairs.emplace_back(i, j);
    uint64_t states = 1;
    for (auto unused : pairs) { (void)unused; states *= 3; }
    uint64_t min_degree_count = 0, metric_count = 0;
    uint64_t old_triangle_count = 0, stronger_triangle_count = 0;
    uint64_t completion_count = 0;
    for (uint64_t state = 0; state < states; ++state) {
      bool edge[6][6] = {};
      std::array<int, 6> out = {};
      uint64_t digits = state;
      for (auto [i, j] : pairs) {
        int value = digits % 3;
        digits /= 3;
        if (value == 1) { edge[i][j] = true; ++out[i]; }
        if (value == 2) { edge[j][i] = true; ++out[j]; }
      }
      bool good = true;
      for (int i = 0; i < n; ++i) if (out[i] < 2) good = false;
      if (!good) continue;
      ++min_degree_count;
      bool metric = true, old_triangles = true, strong_triangles = true;
      for (int i = 0; i < n; ++i)
        for (int j = i + 1; j < n; ++j)
          for (int k = j + 1; k < n; ++k) {
            bool triangle = (edge[i][j] || edge[j][i]) &&
                            (edge[i][k] || edge[k][i]) &&
                            (edge[j][k] || edge[k][j]);
            if (!triangle) continue;
            if (edge[k][i]) metric = false;
            if (edge[i][j] && edge[i][k] && edge[j][k])
              old_triangles = false;
            if (edge[i][j] && edge[i][k]) strong_triangles = false;
          }
      if (!metric) continue;
      ++metric_count;
      if (!old_triangles) continue;
      ++old_triangle_count;
      bool unique_completion = true;
      for (int i = 0; i < n; ++i)
        for (int k = i + 1; k < n; ++k) {
          if (!edge[i][k]) continue;
          int completions = 0;
          for (int j = i + 1; j < k; ++j)
            if (edge[k][j] && edge[j][i]) ++completions;
          if (completions > 1) unique_completion = false;
        }
      if (strong_triangles) ++stronger_triangle_count;
      if (unique_completion) ++completion_count;
    }
    std::cout << "orbits=" << n << " states=" << states
              << " min_outdegree_2=" << min_degree_count
              << " after_metric=" << metric_count
              << " after_no_ascending_triangle=" << old_triangle_count
              << " after_no_smallest_source_triangle=" << stronger_triangle_count
              << " after_unique_reverse_completion=" << completion_count
              << '\n';
    if (completion_count != 0) return 1;
  }
}
