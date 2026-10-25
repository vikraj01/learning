// Small line icons, drawn on a 16×16 grid, coloured by currentColor.

type P = { size?: number };
const svg = (size: number, children: React.ReactNode, strokeWidth = 1.6) => (
  <svg width={size} height={size} viewBox="0 0 16 16" fill="none" stroke="currentColor" strokeWidth={strokeWidth}
    strokeLinecap="round" strokeLinejoin="round" aria-hidden="true">
    {children}
  </svg>
);

export const Logo = ({ size = 22 }: P) => (
  <svg width={size} height={size} viewBox="0 0 24 24" fill="none" stroke="#f7f4ee" strokeWidth="1.6" aria-hidden="true">
    <rect x="3" y="11" width="5" height="5" rx="1" /><rect x="9.5" y="11" width="5" height="5" rx="1" />
    <rect x="16" y="11" width="5" height="5" rx="1" /><rect x="9.5" y="4.5" width="5" height="5" rx="1" />
    <path d="M2 18.5c2.5 2 17.5 2 20 0" />
  </svg>
);
export const Check = ({ size = 16 }: P) => svg(size, <path d="M3.5 8.5l3 3 6-7" />, 2);
export const Cross = ({ size = 16 }: P) => svg(size, <path d="M4.5 4.5l7 7M11.5 4.5l-7 7" />, 2);
export const CheckCircle = ({ size = 16 }: P) => svg(size, <><circle cx="8" cy="8" r="6.5" /><path d="M5 8.2l2 2 4-4.2" /></>);
export const ChevronRight = ({ size = 16 }: P) => svg(size, <path d="M6 3.5L10.5 8 6 12.5" />, 1.8);
export const ChevronLeft = ({ size = 16 }: P) => svg(size, <path d="M10 3.5L5.5 8l4.5 4.5" />, 1.8);
export const ChevronDown = ({ size = 16 }: P) => svg(size, <path d="M3.5 6L8 10.5 12.5 6" />, 1.8);
export const Reset = ({ size = 16 }: P) => svg(size, <><path d="M3 8a5 5 0 1 0 1.6-3.7" /><path d="M3 2.5v3h3" /></>);
export const Refresh = ({ size = 16 }: P) => svg(size, <><path d="M13 8a5 5 0 1 1-1.6-3.7" /><path d="M13 2.5v3h-3" /></>);
export const Bulb = ({ size = 16 }: P) => svg(size, <><path d="M6 12.5h4M6.5 14.5h3" /><path d="M8 1.5a4.5 4.5 0 0 0-2.6 8.2c.4.3.6.7.6 1.2v.6h4v-.6c0-.5.2-.9.6-1.2A4.5 4.5 0 0 0 8 1.5z" /></>);
export const FileIcon = ({ size = 16 }: P) => svg(size, <><path d="M9 1.5H4a1 1 0 0 0-1 1v11a1 1 0 0 0 1 1h8a1 1 0 0 0 1-1V5.5z" /><path d="M9 1.5v4h4" /></>, 1.4);
export const FolderIcon = ({ size = 16 }: P) => svg(size, <path d="M1.5 4a1 1 0 0 1 1-1h3.5l1.5 1.5h6a1 1 0 0 1 1 1V12a1 1 0 0 1-1 1h-11a1 1 0 0 1-1-1z" />, 1.4);
export const NewFile = ({ size = 16 }: P) => svg(size, <><path d="M9 1.5H4a1 1 0 0 0-1 1v11a1 1 0 0 0 1 1h8a1 1 0 0 0 1-1V5.5z" /><path d="M9 1.5v4h4M8 8v4M6 10h4" /></>, 1.4);
export const NewFolder = ({ size = 16 }: P) => svg(size, <><path d="M1.5 4a1 1 0 0 1 1-1h3.5l1.5 1.5h6a1 1 0 0 1 1 1V12a1 1 0 0 1-1 1h-11a1 1 0 0 1-1-1z" /><path d="M8 7v4M6 9h4" /></>, 1.4);
export const Trash = ({ size = 14 }: P) => svg(size, <><path d="M2.5 4.5h11M6 4.5V3h4v1.5M4 4.5l.7 9h6.6l.7-9" /></>, 1.4);
export const Search = ({ size = 16 }: P) => svg(size, <><circle cx="7" cy="7" r="4.5" /><path d="M10.5 10.5l3.5 3.5" /></>, 1.6);
export const GridIcon = ({ size = 15 }: P) => svg(size, <><rect x="2" y="2" width="5" height="5" rx="1" /><rect x="9" y="2" width="5" height="5" rx="1" /><rect x="2" y="9" width="5" height="5" rx="1" /><rect x="9" y="9" width="5" height="5" rx="1" /></>, 1.4);
export const ListIcon = ({ size = 15 }: P) => svg(size, <><rect x="2" y="2.5" width="12" height="4.5" rx="1" /><rect x="2" y="9" width="12" height="4.5" rx="1" /></>, 1.4);
export const RowsIcon = ({ size = 15 }: P) => svg(size, <path d="M2 3.5h12M2 6.5h12M2 9.5h12M2 12.5h12" />, 1.4);
export const Whale = ({ size = 16 }: P) => svg(size, <><rect x="2" y="7" width="3" height="3" rx=".5" /><rect x="5.5" y="7" width="3" height="3" rx=".5" /><rect x="9" y="7" width="3" height="3" rx=".5" /><rect x="5.5" y="3.5" width="3" height="3" rx=".5" /><path d="M1 11.5c1.5 1.5 11 2 14-1.5" /></>, 1.3);
