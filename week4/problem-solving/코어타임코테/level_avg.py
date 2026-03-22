# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        
        # bfs 활용해야 할 듯
        # 이진이니까 deque 하고 다음 레벨 큐에 넣을때 
        # node.value 합치고  /2 해서 rs [] 넣고 
        # return 반환하면 된다고 생각함 

        #inorder 순회 = bfs  방식 이고 노드뺴고 리스트에 0번을 제외한 12,34 인덱스들 
        # rs = (1+2) /2 에 하는 방식도 고려해봄 

        visit = []  # 방문한 노드
        rs = []
        tp = []
        que = deque([root])
        visit.append(root)
        rs.append(root)

        while que: 
            node = que.popleft()
            tp.append(node.value)
            if len(tp) == 2:
                sum = tp[0] + tp[1]
                avg = sum/2
                rs.append(avg)
            for i in 이진트리:
                if node not in visit:
                    que.append(i.value)
                    visit.append(i.value)
        return rs
        
