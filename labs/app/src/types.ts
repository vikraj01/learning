export interface Task {
  id: string;
  title: string;
  hint: string;
}

export interface LabSummary {
  id: string;
  number: number;
  title: string;
  summary: string;
  level: "Easy" | "Medium" | string;
  minutes: number;
  topics: string[];
  tasks: Task[];
  solved: boolean;
  started: boolean;
}

export interface LabDetail extends LabSummary {
  task: string;
  ready: boolean;
  next: { id: string; title: string } | null;
}

export interface CheckResult {
  pass: boolean;
  message: string;
}

export interface CheckResponse {
  solved: boolean;
  results: Record<string, CheckResult>;
}

export interface TreeNode {
  name: string;
  path: string;
  type: "file" | "dir";
  mtime?: number;
  children?: TreeNode[];
}
