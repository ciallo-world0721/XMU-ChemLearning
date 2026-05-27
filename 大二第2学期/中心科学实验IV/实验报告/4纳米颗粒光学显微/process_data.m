% !TEX root = report.tex
% 数据处理脚本：调用课程给出的 Cal_coefficient.m 计算每条轨迹的 MSD、
% 扩散系数 D 和异常扩散指数 alpha，并将结果保存为 CSV，供报告与绘图使用。

clc; clear;
set(0, 'DefaultFigureVisible', 'off');

files = ["1.xlsx"; "2.xlsx"; "3.xlsx"; "3-2.xlsx"; "4.xlsx"; "4-2.xlsx"];
labels = ["第一组"; "第二组"; "第三组"; "第三组-2"; "第四组"; "第四组-2"];
calstep = 150;
pixel_size_nm = 246.8;

summary = table('Size', [numel(files), 6], ...
    'VariableTypes', {'string', 'string', 'double', 'double', 'double', 'double'}, ...
    'VariableNames', {'Sample', 'SourceFile', 'Frames', 'FitTime_s', 'D_nm2_per_s_alpha', 'Alpha'});

all_t = [];
all_msd = [];

for k = 1:numel(files)
    trace = xlsread(fullfile("src", files(k)));
    trace = trace .* pixel_size_nm; % nm
    valid_step = min(calstep, size(trace, 1) - 1);

    [MSD, D, alpha, ~, t] = Cal_coefficient(trace, valid_step);

    summary.Sample(k) = labels(k);
    summary.SourceFile(k) = files(k);
    summary.Frames(k) = size(trace, 1);
    summary.FitTime_s(k) = t(end);
    summary.D_nm2_per_s_alpha(k) = D;
    summary.Alpha(k) = alpha;

    all_t = [all_t; t(:)];
    all_msd = [all_msd; MSD(:)];
    if k == 1
        msd_table = table(repmat(labels(k), numel(t), 1), t(:), MSD(:), ...
            'VariableNames', {'Sample', 't_s', 'MSD_nm2'});
    else
        msd_table = [msd_table; table(repmat(labels(k), numel(t), 1), t(:), MSD(:), ...
            'VariableNames', {'Sample', 't_s', 'MSD_nm2'})];
    end
end

writetable(summary, "data_summary.csv");
writetable(msd_table, "msd_results.csv");
disp(summary);
