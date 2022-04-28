class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def minDistance(self, A, B):
        mem = [[-1 for _ in range(len(B))] for _ in range(len(A))]

        def dp(ia, ib):
            if ia == len(A):
                return len(B) - ib
            
            if ib == len(B):
                return len(A) - ia

            if mem[ia][ib] != -1:
                return mem[ia][ib]

            if A[ia] == B[ib]:
                mem[ia][ib] = dp(ia+1, ib+1)
                return mem[ia][ib]
            else:
                inse = dp(ia, ib+1)
                dele = dp(ia+1, ib)
                chan = dp(ia+1, ib+1)

                # +1 because performing any of these operations increases 1 step
                mem[ia][ib] = min(inse, dele, chan) + 1

                return mem[ia][ib]
        
        return dp(0, 0)