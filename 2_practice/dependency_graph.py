import requests
from graphviz import Digraph
import sys

def get_dependencies(package):
    dependencies = []
    response = requests.get(f'https://pypi.org/pypi/{package}/json')
    if response.status_code == 200:
        data = response.json()
        # print(data)
        requires_dist = data['info'].get('requires_dist', None)
        if requires_dist is None:
            requires_dist = []
        for requirement in requires_dist:
            if 'extra' not in requirement:
                dependencies.append(requirement.split()[0])
    return dependencies


def build_dependency_graph(package_name):
    graph = Digraph(package_name)
    visited = set()

    def dfs(package):
        if package in visited:
            return
        visited.add(package)
        dependencies = get_dependencies(package)
        for dependency in dependencies:
            dependency_package = dependency.split(' ')[0]
            graph.edge(package, dependency_package)
            dfs(dependency_package)

    dfs(package_name)
    return graph

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python dependency_graph.py <package_name>")
        sys.exit(1)

    package_name = sys.argv[1]

    graph = build_dependency_graph(package_name)
    print(graph)























# import requests
# from graphviz import Digraph
# #Pandas
# #Requests
# #Написать на выбранном вами языке программирования программу,
# # которая принимает в качестве аргумента командной строки имя пакета,
# # а возвращает граф его зависимостей в виде текста на языке Graphviz.
# # На выбор: для npm или для pip. Пользоваться самими этими менеджерами пакетов запрещено.
# # Главное, чтобы программа работала даже с неустановленными пакетами и без использования pip/npm.
# def get_package_dependencies(package_name):
#     url = f'https://pypi.org/pypi/{package_name}/json'
#     response = requests.get(url)
#     if response.status_code == 200:
#         package_data = response.json()
#         dependencies = package_data['info']['requires_dist']
#         return dependencies if dependencies is not None else []
#     else:
#         print(f'Failed to get dependencies for {package_name}')
#         return []
#
#
# def create_dependency_graph(package_name):
#     graph = Digraph(package_name)
#     visited = set()
#
#     def dfs(package):
#         if package in visited:
#             return
#         visited.add(package)
#         dependencies = get_package_dependencies(package)
#         for dependency in dependencies:
#             dependency_package = dependency.split(' ')[0]
#             graph.edge(package, dependency_package)
#             dfs(dependency_package)
#
#     dfs(package_name)
#     return graph
#
# if __name__ == '__main__':
#     package_name = input('Enter package name: ')
#     graph = create_dependency_graph(package_name)
#     print(graph.source)