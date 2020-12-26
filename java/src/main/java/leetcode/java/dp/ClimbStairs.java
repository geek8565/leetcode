package leetcode.java.dp;

public class ClimbStairs {
	
	/*
	 * 假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
	 * 每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
	 */
	
	/*
	 * 	这是一个动态规划问题：
	 * 	1.找到初始条件 x0=0 y0=0, x1=1 y1=1, x2=2 y2=2, x3=3 y3=y1+y2;
	 * 	2.找到表达式 f(x)=f(x−1)+f(x−2)
	 */
	
	public Integer process(int n) {
		// 边界处理
		if(n<=0) {
			return 0;
		}
		// 正式处理
		int first = 0, second = 0, result = 1;
        for (int i = 1; i <= n; ++i) {
            first = second; 
            second = result; 
            result = first + second;
        }
        return result;
	}
	
	public static void main(String[] args) throws Exception {
		ClimbStairs engine = new ClimbStairs();
		int input = 4;
		Integer result = engine.process(input);
		System.out.println("楼梯数量：" + input + "; 有 " + result + " 种方法爬完！");
	}
}
