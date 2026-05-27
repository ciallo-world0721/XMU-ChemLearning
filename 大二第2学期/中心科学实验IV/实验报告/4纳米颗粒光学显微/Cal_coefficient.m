function [MSD,D,alpha,myfit,t] = Cal_coefficient(trace,calstep)

% 计算轨迹的特征指标，包括均方位移MSD, 扩散系数D， 异常指数alpha， 拟合结果等

% trace : 输入轨迹位置数据    M * 2, M代表轨迹长度
% calstep : 进行alpha计算的有效数据

row = size(trace,1);
times = 0.02 * (1:row);
n = row-1;

% 计算距离
distance = zeros(n,n);
for i = 2:row
    for j = 1:i-1
        distance(i-1,i-j) = (norm(trace(i,:,:)-trace(j,:,:)))^2;
    end
end

% 计算平均MSD
MSD = zeros(1,n);
for i = 1:n
    MSD(1,i) = sum(distance(:,i))/(row-i);
end

% fitting，计算alpha
t = times(1:calstep);
myfittype = fittype('s*(t^alpha)','independent','t','coefficients',{'s','alpha'},'dependent',{'MSD'});
myfit = fit(t',MSD(1,1:calstep)',myfittype);
warning off
alpha = myfit.alpha;

% 扩散系数D的计算
K = myfit.s;
D = K / 4;
MSD = MSD(1:calstep);

figure
plot(myfit,t,MSD)



