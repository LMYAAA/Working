package com.liujun.static_agent;

/**
 * 总结：
 * 真实对象和代理对象都要实现同一个接口
 * 代理对象要代理真实角色
 * 好处：
 * 代理对象可以做好多真实对象做不了的事情，真实对象可以专注做自己的事情
 */
public class StacticProxy {
    public static void main(String[] args) {
        new Thread( ()-> System.out.println("我爱你")).start();
        new WeddingCompany(new You()).HappyMarry();

//        You you = new You();    // 你要结婚
//        WeddingCompany weddingCompany = new WeddingCompany(you);
//        weddingCompany.HappyMarry();
    }
}

interface Marry{
    void HappyMarry();
}

// 真实角色,你去结婚
class You implements Marry{

    @Override
    public void HappyMarry() {
        System.out.println("秦老师结婚了，超开心");
    }
}

// 代理角色，帮助你结婚
class WeddingCompany implements Marry{
    // 代理谁-->真实目标角色
    private Marry target;

    public WeddingCompany(Marry target) {
        this.target = target;
    }

    @Override
    public void HappyMarry() {
        before();
        this.target.HappyMarry();
        after();
    }

    private void after() {
        System.out.println("结婚之后收尾款");
    }

    private  void before(){
        System.out.println("结婚之前布置现场");
    }
}
