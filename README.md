# Ubereats 平台端模擬

## Ubereats 流程
1. 收到消費者客戶端的訂單，但為了方便模擬，所以設計成**手動新增訂單**
2. 平台端收到訂單後，**發派給店家**，此專案不模擬店家收單與準備餐點的階段，發派後即完成餐點
3. 完成餐點後，**發派給司機**，把餐點運送至消費者手中，此專案也不模擬司機送至消費者的階段，發派後即完成送達餐點
4. 「發派餐點」與「發派司機」兩者都完成後，則自動**完成訂單**

## Usage

##### 如果沒有 pipenv
```python
pip install pipenv
```

#### 進入虛擬環境
```python
pipenv shell
```

#### 啟動伺服器
```python
python manage.py runserver
```

#### Django 內建後台登入
進入 http://127.0.0.1:8000/admin

帳號: root
密碼: admin