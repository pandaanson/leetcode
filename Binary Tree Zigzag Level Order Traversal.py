result = []

        def dfs(node, level):
            if not node:
                return
            # Expand result list if needed
            if len(result) == level:
                result.append([])
            # Append current node's value to the corresponding sublist
            if level % 2 == 0:
                result[level].append(node.val)
            else:
                result[level].insert(0, node.val)
            # Recurse on child nodes
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)

        dfs(root, 0)
        return result
