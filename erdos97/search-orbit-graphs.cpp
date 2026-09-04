// Exact search over oriented graphs with outdegree exactly two.
// Hereditary necessary conditions make this sufficient for existence with
// minimum outdegree at least two: delete outgoing edges down to two each.
// Vertices are ordered by increasing radius (ties may be ordered arbitrarily).
#include <array>
#include <cstdint>
#include <cstdlib>
#include <fstream>
#include <iostream>
#include <string>

int n;
bool edge[9][9] = {};
uint64_t visited = 0, solutions = 0;
std::array<uint64_t, 10> by_depth = {};
bool first_only = false;
std::ofstream graph_dump;

bool consistent() {
  for (int i = 0; i < n; ++i)
    for (int j = i + 1; j < n; ++j) {
      if (edge[i][j] && edge[j][i]) return false;
      for (int k = j + 1; k < n; ++k) {
        const bool complete = (edge[i][j] || edge[j][i]) &&
                              (edge[i][k] || edge[k][i]) &&
                              (edge[j][k] || edge[k][j]);
        if (complete && (edge[k][i] || (edge[i][j] && edge[i][k])))
          return false;
      }
      if (!edge[i][j]) continue;
      int completions = 0;
      for (int k = i + 1; k < j; ++k)
        if (edge[j][k] && edge[k][i] && ++completions > 1)
          return false;
    }
  return true;
}

bool search(int row) {
  ++visited;
  ++by_depth[n - 1 - row];
  if (row < 0) {
    ++solutions;
    if (graph_dump) {
      graph_dump << '[';
      for (int i = 0; i < n; ++i) {
        unsigned mask = 0;
        for (int j = 0; j < n; ++j) if (edge[i][j]) mask |= 1u << j;
        if (i) graph_dump << ',';
        graph_dump << mask;
      }
      graph_dump << "]\n";
    }
    if (solutions == 1) {
      std::cout << "First abstract graph (not coordinates):\n";
      for (int i = 0; i < n; ++i) {
        std::cout << i << ':';
        for (int j = 0; j < n; ++j) if (edge[i][j]) std::cout << ' ' << j;
        std::cout << '\n';
      }
    }
    return first_only;
  }
  for (int a = 0; a < n; ++a) {
    if (a == row || edge[a][row]) continue;
    for (int b = a + 1; b < n; ++b) {
      if (b == row || edge[b][row]) continue;
      edge[row][a] = edge[row][b] = true;
      bool stop = consistent() && search(row - 1);
      edge[row][a] = edge[row][b] = false;
      if (stop) return true;
    }
  }
  return false;
}

int main(int argc, char** argv) {
  n = argc > 1 ? std::atoi(argv[1]) : 7;
  first_only = argc > 2 && std::string(argv[2]) == "first";
  if (n < 3 || n > 9) return 2;
  if (argc > 3 && std::string(argv[2]) == "dump") {
    graph_dump.open(argv[3]);
    if (!graph_dump) return 3;
  }
  search(n - 1);
  std::cout << "orbits=" << n << " recursive_nodes=" << visited
            << " solutions=" << solutions
            << " exhaustive=" << (!first_only || solutions == 0) << '\n';
  std::cout << "consistent_prefixes_by_assigned_row_count:";
  for (int i = 0; i <= n; ++i) std::cout << ' ' << by_depth[i];
  std::cout << '\n';
}
