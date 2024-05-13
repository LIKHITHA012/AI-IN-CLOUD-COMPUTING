import math  # Import the math module for logarithmic function

def minimax(curDepth, nodeIndex, maxTurn, scores, targetDepth):
    # Base case: If current depth reaches the target depth, return the score
    if curDepth == targetDepth:
        return scores[nodeIndex]

    if maxTurn:
        # Maximizer's turn: Choose the maximum value from child nodes
        leftChild = minimax(curDepth + 1, nodeIndex * 2, False, scores, targetDepth)
        rightChild = minimax(curDepth + 1, nodeIndex * 2 + 1, False, scores, targetDepth)
        return max(leftChild, rightChild)
    else:
        # Minimizer's turn: Choose the minimum value from child nodes
        leftChild = minimax(curDepth + 1, nodeIndex * 2, True, scores, targetDepth)
        rightChild = minimax(curDepth + 1, nodeIndex * 2 + 1, True, scores, targetDepth)
        return min(leftChild, rightChild)

# Example usage
scores = [3, 5, 2, 9, 12, 5, 23, 23]
treeDepth = math.log(len(scores), 2)  # Calculate the depth of the binary tree
print("The optimal value is:", end=" ")
result = minimax(0, 0, True, scores, int(treeDepth))
print(result)

